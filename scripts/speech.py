#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/speech.py
#

# Imports
import argparse
import time
#import urllib
from naoqi import ALProxy

def main(IP, PORT):
	tts = ALProxy("ALTextToSpeech", IP, PORT)
	tts.setVolume(0.8)  ##Volume set to 80%
    	tts.setParameter("pitchShift", 1.2) #Applies a pitch shifting to the voice
    	tts.setParameter("doubleVoice", 0.0) #Deactivates double voice
    

	move= ALProxy("ALAutonomousMoves", IP, PORT)
	move.setExpressiveListeningEnabled(False)


	##TESTING		

	#colour(IP,PORT,tts)
    
	#colour=Rec(IP,PORT,tts)
	#brick,number=colour
        #print brick,number
        

def Rec(IP,PORT,tts):
    data=[]
    # Creates a proxy on the speech-recognition module
    asr = ALProxy("ALSpeechRecognition",IP, PORT)
    memProxy = ALProxy("ALMemory",IP,PORT)
    asr.pause(True)
    asr.setLanguage("English")

    vocabulary = ["Green", "Yellow", "Blue", "Red","Green Brick","Pick Green Brick","Pick Up Green Brick","Please Pick Up Green Brick"]
    asr.setVocabulary(vocabulary, False)

    # Start the speech recognition engine with user Test_ASR
    tts.say("I am listening")
    asr.subscribe("Test_ASR")
    print 'Speech recognition engine started'
    asr.pause(False)
    time.sleep(3)
    data=memProxy.getData("WordRecognized")
    asr.unsubscribe("Test_ASR")
 
    return data


def colour(IP,PORT,tts):
    while True:
        colour=Rec(IP,PORT,tts)
        brick,number=colour
        print brick,number
        if number!=-3:
            break
        else:
            continue
    return brick




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)



