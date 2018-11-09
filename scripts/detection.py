#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/detection.py
#

# Imports
import argparse
import time
import numpy as np
import cv2
from naoqi import ALProxy
from PIL import Image
#import naoqi
#import PIL
#import math

#Importing scripts
import Hand


def main(IP, PORT):
	blockwidth = 4
	proxy = ALProxy("ALMotion",IP,PORT)
    	#proxy.wakeUp()

	tts = ALProxy("ALTextToSpeech", IP, PORT)
    	tts.setVolume(1.5)  ##Volume set to 100%
   	tts.setParameter("pitchShift", 1.2) #Applies a pitch shifting to the voice
    	tts.setParameter("doubleVoice", 0.0) #Deactivates double voice
 
	################################
	##TESTING		
	
	###########
	###TESTING: def getframe(IP,PORT,flag):
	#img=getframe(IP,PORT)
	#print(img)

	#showimage(img)

	#Applying Grayscale filter to image
	#gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
	#cv2.imwrite('graytest.jpg',gray)
	#[x] https://docs.python-guide.org/scenarios/imaging/

	##########
	###TESTING: def target(IP,PORT,LH,LS,LV,UH,US,UV,tts):
       	#LH,LS,LV,UH,US,UV=50,55,5,105,255,255	##if colour=='Green':
        #LH,LS,LV,UH,US,UV=107,50,50,130,255,255 ##elif colour=='Blue': 
	#d=target(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
	#print(d)


	##########
	###TESTING: def getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts):
       	#LH,LS,LV,UH,US,UV=50,55,5,105,255,255	##if colour=='Green':
       	#LH,LS,LV,UH,US,UV=107,50,50,130,255,255 ##elif colour=='Blue':
	#cx,cy=getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
	#print(cx,cy)

	##########
	###TESTING: 	def hand(IP,PORT):
	#h=hand(IP,PORT,tts,showingimage=True)
	#print(h)


	##########
	###TESTING: #def recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV):
	#x,y=0,0
       	##LH,LS,LV,UH,US,UV=50,55,5,105,255,255	##if colour=='Green':
        #LH,LS,LV,UH,US,UV=107,50,50,130,255,255 ##elif colour=='Blue':	
	#Left_H,Right_H=1,0 ##Left Hand, Right Hand
	#CK=2
	#a,b=recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV,tts)
	#print(a,b)

    	##proxy.rest() # Go to rest pose 


def getframe(IP,PORT):
	flag=1
	camProxy = ALProxy("ALVideoDevice", IP, PORT)
    	resolution = 2   # VGA
    	colorSpace = 11  # RGB
   
    	camProxy.setParam(18, flag)
    	videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
    	# Get a camera image.
    	t0 = time.time()
    	# Time the image transfer.
    	#print "acquisition delay ", t1 - t0
    	naoImage = camProxy.getImageRemote(videoClient)
    	t1 = time.time()
    	camProxy.unsubscribe(videoClient)
    	# Set the image size and pixel array.
    	imageWidth = 640
    	imageHeight = 480
    	array = naoImage[6]
    	# Create a PIL Image from our pixel array.
    	#im = Image.fromstring("RGB", (imageWidth, imageHeight), array) 
	#Error	https://stackoverflow.com/questions/38497924/capturing-image-from-webcam-using-python-on-windows
    	im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
    	ci = np.array(im)  
    	r, g, b = cv2.split(ci) 
    	ci = cv2.merge([b, g, r])

	return ci

def target(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=False):
    	detection=0
    	image=getframe(IP,PORT)
    	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	##define range of green color in HSV
    	#lower_green = np.array([50,55,5])
    	#upper_green = np.array([105,255,255])
    	#lower_blue = np.array([110,50,50])
    	#upper_blue = np.array([130,255,255])
    
    	lower_colo = np.array([LH,LS,LV])
    	upper_colo = np.array([UH,US,UV])
    	mask = cv2.inRange(hsv, lower_colo, upper_colo)	
    	resf=cv2.medianBlur(mask,5)
	
    	ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    	img2, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    	

	area_threshold=2000 # this threshold migth change according to light conditions
	for contour in contours:
        	area = cv2.contourArea(contour)
        	d=cv2.minAreaRect(contour) # returns ( center (x,y), (width, height), angle of rotation )
        	cen=d[1]
 		#print(area)
 		#print(d)
 		#print(cen)
	
		if area > area_threshold:
                		detection=1
                		print("area",area)
                		tts.say("I see a LEGO brick")
	
				if showingimage == True:
					cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
 					showimage(image)



	return detection


#def check(IP,PORT,LH,LS,LV,UH,US,UV):
#    detection=0
#    image=getframe(IP,PORT)
#    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
#    # define range of green color in HSV
#    #lower_green = np.array([50,55,5])
#    #upper_green = np.array([105,255,140])
#    #mask = cv2.inRange(hsv, lower_green, upper_green)
#    
#    lower_colo = np.array([LH,LS,LV])
#    upper_colo = np.array([UH,US,UV])
#    mask = cv2.inRange(hsv, lower_colo, upper_colo)
#    resf=cv2.medianBlur(mask,5)
#
#    ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
#    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#    
#    for i in range(len(contours)):
#        area=cv2.contourArea(contours[i])
#        d=cv2.minAreaRect(contours[i])
#        cen=d[1]
#        if  area>5000 and area<16000:
#            detection=1
#            print("area",area)
#            tts.say("I see the brick")
#    return detection
#



def getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=False):
	x=y=z=0
	detection=0
	image=getframe(IP,PORT)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	lower_colo = np.array([LH,LS,LV])
	upper_colo = np.array([UH,US,UV])
	mask = cv2.inRange(hsv, lower_colo, upper_colo)
	resf=cv2.medianBlur(mask,5)
	
    	ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    	img2, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)    	
 	#showimage(binary)

	area_threshold=2000 # this threshold migth change according to light conditions
	for contour in contours:
        	area = cv2.contourArea(contour)
        	d=cv2.minAreaRect(contour) # returns ( center (x,y), (width, height), angle of rotation )
        	cen=d[1]
 		#print(area)
 		#print(d)
 		#print(cen)
	
		if area > area_threshold:
                		detection=1
                		print("area",area)
                		tts.say("I see a LEGO brick")
	
				if showingimage == True:
					cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
 					showimage(image)


				c=cv2.moments(contour)
				#Image moments help you to calculate some features like 
				#centroid which is given by the relationship
				# See https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
		        	cx=c['m10']/c['m00']
				cy=c['m01']/c['m00']
				x=round(cx,2)
				y=round(cy,2)
				#print('~cx', x)
				#print('~cy', y)
		else:
			#tts.say("I can not see the green brick")
			print("error")
	
	return (x,y)




def hand(IP,PORT,tts,showingimage=False):
	findhand=0
    	image=getframe(IP,PORT)
    	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	# define range of green color in HSV
    	lower_green = np.array([5,45,5])
    	upper_green = np.array([12,255,255])
   	
    	mask = cv2.inRange(hsv, lower_green, upper_green)
    	
    	resf=cv2.medianBlur(mask,5)

	ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    	img2, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   
	area_threshold=22000 # this threshold migth change according to light conditions
	for contour in contours:
        	area = cv2.contourArea(contour)
        	d=cv2.minAreaRect(contour) # returns ( center (x,y), (width, height), angle of rotation )
        	cen=d[1]
 		print(area)
 		#print(d)
 		#print(cen)
	
		if area > area_threshold:
                		findhand=1
                		print("area",area)
                		tts.say("I see your hand")
	
				if showingimage == True:
					cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
 					showimage(image)



	return findhand


 

def recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV,tts):
	if CK==1:
		Hand.choose(IP,PORT,Left_H,Right_H)
        	pick_flag=True
        	again_flag=False
    	else:
        	#nx,ny=getcenter(IP,PORT,LH,LS,LV,UH,US,UV)
		nx,ny=getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
        	if nx<=x+25 and nx>=x-25 and ny<=y+25 and ny>=y-25:
            		Hand.choose(IP,PORT,Left_H,Right_H)
            		pick_flag=True
            		again_flag=False
            		print("step")
        	else:
            		pick_flag=False
            		again_flag=True
            		print("step2")
	
	return pick_flag,again_flag
    




def showimage(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)






