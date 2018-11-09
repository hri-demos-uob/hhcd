#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/Hand.py



# Imports
import argparse
import time
from naoqi import ALProxy

#Importing scripts
import arm



def main(IP, PORT):
	proxy = ALProxy("ALMotion",IP,PORT)


	#################################
	###TESTING
	#LH,RH=0,1 #Left Hand  #Right Hand
	#a=choose(IP,PORT,LH,RH)
	#print(a)

    	#proxy.rest() # Go to rest pose 


def choose(IP,PORT,LH,RH):
	proxy = ALProxy("ALMotion",IP,PORT)
	names = "Body"
	stiffness = 1.0
	proxy.stiffnessInterpolation(names, stiffness, 1.0)
	proxy.setAngles("HeadPitch",0.157,0.2)

	if LH==1: #Left Hand
        	proxy.setAngles("LHand",0.25,0.2)
        	time.sleep(0.5)
        	arm.Left_Arm(IP,PORT,proxy)
        	time.sleep(0.5)
        	pick_flag=True
    	elif RH==1: #Right Hand
        	proxy.setAngles("RHand",0.25,0.2)
        	time.sleep(0.5)
        	arm.Right_Arm(IP,PORT,proxy)
        	time.sleep(0.5)
        	pick_flag=True
    	else:
        	pick_flag=False
    	
	return pick_flag




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)




