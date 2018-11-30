#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/Arm.py
#

# Imports
import time
from naoqi import ALProxy


def Reset(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
   	proxy.setAngles("RShoulderPitch",0.42,fms)
    	proxy.setAngles("RShoulderRoll",-0.8,fms)
	proxy.setAngles("RElbowYaw",0.16,fms)
	proxy.setAngles("RElbowRoll",0.94,fms)
    	proxy.setAngles("RWristYaw",1.33,fms)
	proxy.setAngles("RHand",1,fms)

	proxy.setAngles("LShoulderPitch",0.37,fms)
	proxy.setAngles("LShoulderRoll",0.8,fms)
	proxy.setAngles("LElbowYaw",-0.16,fms)
	proxy.setAngles("LElbowRoll",-0.94,fms)
    	proxy.setAngles("LWristYaw",-1.33,fms)
	proxy.setAngles("LHand",1,fms)


def B1(IP,PORT,proxy):
    proxy.setAngles("LShoulderPitch",0.38,0.2)
    proxy.setAngles("LShoulderRoll",0.1,0.2)
    proxy.setAngles("LElbowYaw",-0.4,0.2)
    proxy.setAngles("LElbowRoll",-0.56,0.2)
    proxy.setAngles("LWristYaw",-1.22,0.2)

def B2(IP,PORT,proxy):
    proxy.setAngles("LShoulderPitch",0.35,0.2)
    proxy.setAngles("LShoulderRoll",-0.15,0.2)
    proxy.setAngles("LElbowYaw",-0.3,0.2)
    proxy.setAngles("LElbowRoll",-0.4,0.2)
    proxy.setAngles("LWristYaw",-1.3,0.2)

def B3(IP,PORT,proxy):
    proxy.setAngles("RShoulderPitch",0.38,0.2)
    proxy.setAngles("RShoulderRoll",0.15,0.2)
    proxy.setAngles("RElbowYaw",0.3,0.2)
    proxy.setAngles("RElbowRoll",0.4,0.2)
    proxy.setAngles("RWristYaw",1.3,0.2)

def B4(IP,PORT,proxy):
    proxy.setAngles("RShoulderPitch",0.4,0.2)
    proxy.setAngles("RShoulderRoll",-0.14,0.2)
    proxy.setAngles("RElbowYaw",0.3211,0.2)
    proxy.setAngles("RElbowRoll",0.6981,0.2)
    proxy.setAngles("RWristYaw",1.22,0.2)

def C1(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
	proxy.setAngles("LShoulderRoll",0.31,fms)
	proxy.setAngles("LShoulderPitch",0.31,fms)
	proxy.setAngles("LElbowYaw",0,fms)
	proxy.setAngles("LElbowRoll",-0.98,fms)
	proxy.setAngles("LWristYaw",-1.48,fms)

def C2(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
	proxy.setAngles("LShoulderPitch",0.31,fms)
	proxy.setAngles("LShoulderRoll",0.09,fms)
	proxy.setAngles("LElbowYaw",-0.05,fms)
	proxy.setAngles("LElbowRoll",-0.9,fms)
	proxy.setAngles("LWristYaw",-1.48,fms)

def C3(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
	proxy.setAngles("RShoulderPitch",0.35,fms)
	proxy.setAngles("RShoulderRoll",-0.09,fms)
	proxy.setAngles("RElbowYaw",0.05,fms)
	proxy.setAngles("RElbowRoll",0.9,fms)
	proxy.setAngles("RWristYaw",1.48,fms)

def C4(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
	proxy.setAngles("RShoulderPitch",0.4,fms)
	proxy.setAngles("RShoulderRoll",-0.3,fms)
	proxy.setAngles("RElbowYaw",0.0802,fms)
	proxy.setAngles("RElbowRoll",0.98,fms)
	proxy.setAngles("RWristYaw",1.48,fms)

def D1(IP,PORT,proxy):
    proxy.setAngles("LShoulderPitch",0.4,0.2)
    proxy.setAngles("LShoulderRoll",0.46,0.2)
    proxy.setAngles("LElbowYaw",-0.082,0.2)
    proxy.setAngles("LElbowRoll",-1.29,0.2)
    proxy.setAngles("LWristYaw",-1.31,0.2)

def D2(IP,PORT,proxy):
    proxy.setAngles("LShoulderPitch",0.4,0.2)
    proxy.setAngles("LShoulderRoll",0.18,0.2)
    proxy.setAngles("LElbowYaw",-0.08,0.2)
    proxy.setAngles("LElbowRoll",-1.22,0.2)
    proxy.setAngles("LWristYaw",-1.3,0.2)

def D3(IP,PORT,proxy):
    proxy.setAngles("RShoulderPitch",0.438,0.2)
    proxy.setAngles("RShoulderRoll",-0.1833,0.2)
    proxy.setAngles("RElbowYaw",0.0820,0.2)
    proxy.setAngles("RElbowRoll",1.22,0.2)
    proxy.setAngles("RWristYaw",1.2985,0.2)

def D4(IP,PORT,proxy):
    proxy.setAngles("RShoulderPitch",0.44,0.2)
    proxy.setAngles("RShoulderRoll",-0.4381,0.2)
    proxy.setAngles("RElbowYaw",0.0820,0.2)
    proxy.setAngles("RElbowRoll",1.2898,0.2)
    proxy.setAngles("RWristYaw",1.3107,0.2)

## hold it
def Right_Arm(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
	proxy.setAngles("RShoulderPitch",-0.4189,fms)
	proxy.setAngles("RShoulderRoll",0.3142,fms)
	proxy.setAngles("RElbowYaw",-0.349,fms)
	proxy.setAngles("RElbowRoll",0.349,fms)
	proxy.setAngles("RWristYaw",0.978,fms)

def Left_Arm(IP,PORT,proxy):
	fms=0.1#fraction maximum speed
	proxy.setAngles("LShoulderPitch",-0.4189,fms)
	proxy.setAngles("LShoulderRoll",-0.3142,fms)
	proxy.setAngles("LElbowYaw",0.6283,fms)
	proxy.setAngles("LElbowRoll",-0.349,fms)
	proxy.setAngles("LWristYaw",-0.978,fms)



