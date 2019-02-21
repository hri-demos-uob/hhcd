#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
#
#

#Imports
import argparse
from naoqi import ALProxy
import time


def main(IP, PORT):

	tts = ALProxy("ALTextToSpeech", IP, PORT)
	tts.say("I am going to rest. Put away the table") 

	proxy = ALProxy("ALMotion",IP,PORT)
    	proxy.rest() # Go to rest pose 
           
	

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)





        
