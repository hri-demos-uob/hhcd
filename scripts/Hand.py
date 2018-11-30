#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/Hand.py

# Imports
import time
from naoqi import ALProxy

#Importing scripts
import Arm




def choose(IP,PORT,LH,RH,proxy):

	proxy.setAngles("HeadPitch",0.157,0.2)

	if LH==1: #Left Hand
        	proxy.setAngles("LHand",0.25,0.1)
        	time.sleep(0.5)
        	Arm.Left_Arm(IP,PORT,proxy)
        	time.sleep(0.5)
        	pick_flag=True
    	elif RH==1: #Right Hand
        	proxy.setAngles("RHand",0.25,0.1)
        	time.sleep(0.5)
        	Arm.Right_Arm(IP,PORT,proxy)
        	time.sleep(0.5)
        	pick_flag=True
    	else:
        	pick_flag=False
    	
	return pick_flag





