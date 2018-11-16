#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/main.py
#

#Imports
import argparse
import math
import numpy
import cv2
from naoqi import ALProxy
import time

#Importing scripts
import detection
import Arm
import MoveArm
import Hand

import sys 
sys.path.insert(0,'..')
from functions import *


def main(IP, PORT):

	tts = ALProxy("ALTextToSpeech", IP, PORT)

	proxy = ALProxy("ALMotion",IP,PORT)
	#names = "Body"
	names = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand']
	stiffness = 1.0
	proxy.stiffnessInterpolation(names, stiffness, 1.0)
	proxy.setAngles("HeadPitch",0.157,0.2)
	Arm.Reset(IP,PORT,proxy)

	nao_collaboration(IP,PORT,tts)
	#nao_relax_body(IP,PORT)


def supermain(IP,PORT,LH,LS,LV,UH,US,UV):
	tts = ALProxy("ALTextToSpeech", IP, PORT)
	proxy = ALProxy("ALMotion",IP,PORT)
	finish=False
    	Arm.Reset(IP,PORT,proxy)
    	Hand_flag=False
    	break_all=False
    	again_flag=False
    	Right_H=0
    	Left_H=0
    	tts.say("I am waiting!")
	time.sleep(2)
    	target=detection.target(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
    	print ("target",target)

    
	while target==1:# main loop
	    	#target=detection.target(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=False)
    		#print ("target",target)

		x,y=detection.getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
		print(x,y)
		Left_H,Right_H=MoveArm.movementX(IP,PORT,x,y,tts,proxy)
		print(Left_H,Right_H)
		time.sleep(1)
	        Hand_flag = True
		
		if Hand_flag==True:
			target_hand=0
			pick_flag=False
			CK=detection.check(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
			print("check",CK)
			pick_flag,again_flag=detection.recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV,tts)
			print pick_flag,again_flag


		if again_flag==True:# try again
			continue
		while pick_flag==True:
			target_hand=detection.hand(IP,PORT,tts,showingimage=False)
			print("hand",target_hand)
			if target_hand==1:
				tts.say("I will relesae it")
				while Right_H==1:
					proxy.setAngles("RHand",1,0.2)
					proxy.setAngles("RShoulderPitch",-0.087,0.2)
					tts.say("I finish the job")
					Arm.Reset(IP,PORT,proxy)
					Right_H=0
					pick_flag=False
					target=0
					finish=True
					continue
				
				while Left_H==1:
					proxy.setAngles("LHand",1,0.2)
					#proxy.setAngles("LShoulderPitch",-0.087,0.2)
					tts.say("I finish the job")
					Arm.Reset(IP,PORT,proxy)
					Left_H=0
					pick_flag=False
					target=0
					finish=True
					continue
        
        return finish
                    
          
 
def nao_inclined_head(IP,PORT):
	proxy = ALProxy("ALMotion",IP,PORT)
	names = "Body"
	stiffness = 1.0
	proxy.stiffnessInterpolation(names, stiffness, 1.0)
	proxy.setAngles("HeadPitch",0.157,0.2)


def nao_relax_body(IP,PORT):
	proxy = ALProxy("ALMotion",IP,PORT)
    	proxy.rest() # Go to rest pose 

           


def nao_collaboration(IP, PORT, tts):

	move= ALProxy("ALAutonomousMoves", IP, PORT)
	move.setExpressiveListeningEnabled(False)
	
	while True:
		#colour=speech.colour(IP,PORT,tts)
		speechcolour=colour(IP,PORT,tts)
 		if speechcolour=='Green':
			print('Green')
			LH,LS,LV=50,55,5
			UH,US,UV=105,255,255
			finish_flag=supermain(IP,PORT,LH,LS,LV,UH,US,UV)
		elif speechcolour=='Blue':
			LH,LS,LV=107,50,50
			UH,US,UV=130,255,255
			finish_flag=supermain(IP,PORT,LH,LS,LV,UH,US,UV)
		        if finish_flag==True:
		            tts.say("I will pick next one")
		            continue
 



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)


#IP = "169.254.67.145"



        
