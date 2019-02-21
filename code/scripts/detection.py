#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/detection.py
#

# Imports
#import argparse
import time
import numpy as np
import cv2
from naoqi import ALProxy
from PIL import Image


#Importing scripts
import Hand

# global variables
bg = None


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
    	image = cv2.merge([b, g, r])

	return image

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


def check(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=False):
	detection=0
	image=getframe(IP,PORT)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	# define range of green color in HSV
    	#lower_green = np.array([50,55,5])
    	#upper_green = np.array([105,255,140])
    	#mask = cv2.inRange(hsv, lower_green, upper_green)
    
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
        	#if  area>5000 and area<16000:
                		detection=1
                		print("area",area)
                		tts.say("I see a LEGO brick")
	
				if showingimage == True:
					cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
 					showimage(image)

	
	return detection




def getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=False):
	#nao_inclined_head(IP,PORT)
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

	
	#nao_relax_body(IP,PORT)
	
	return (x,y)




def hand(IP,PORT,tts,showingimage=False):
	findhand=0
    	image=getframe(IP,PORT)

	#testing equalised value    		
	#showimage(image)
	#ei=hsv_equalized(image)
	#showimage(ei)

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		
	# define range of green color in HSV
    	lower_green = np.array([5,45,5])
    	upper_green = np.array([12,255,255])
   	
    	mask = cv2.inRange(hsv, lower_green, upper_green)
    	
    	resf=cv2.medianBlur(mask,5)

	#showimage(resf)


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


 

def recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV,tts,proxy):
	if CK==1:
		Hand.choose(IP,PORT,Left_H,Right_H,proxy)
        	pick_flag=True
        	again_flag=False
    	else:
        	#nx,ny=getcenter(IP,PORT,LH,LS,LV,UH,US,UV)
		nx,ny=getcenter(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
        	if nx<=x+25 and nx>=x-25 and ny<=y+25 and ny>=y-25:
            		Hand.choose(IP,PORT,Left_H,Right_H,proxy)
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


	#Applying Grayscale filter to image
	#gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
	#cv2.imwrite('graytest.jpg',gray)
	#[x] https://docs.python-guide.org/scenarios/imaging/



## One way to deal with the variation of lighting is normalising the lightligin 
## by equalising the contrast of the images 
## [1](http://answers.opencv.org/question/9054/color-constancy-in-different-illumination-condition/)

## An alternative is to first convert the image to the HSL or HSV color space 
## and then apply the histogram equalization only on the lightness or value 
## channel by leaving the hue and the saturation of the image unchanged. 
## Here's the code that applies the histogram equalization on the value 
## channel of the HSV color space:
## [1](https://lmcaraig.com/image-histograms-histograms-equalization-and-histograms-comparison/)

def hsv_equalized(image):
	H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
	eq_V = cv2.equalizeHist(V)
	eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2RGB)
    	
	return eq_image

	
#-------------------------------------------------------------------------------
# Function - To find the running average over the background
#-------------------------------------------------------------------------------
def run_avg(image, aWeight):
    global bg
    # initialize the background
    if bg is None:
        bg = image.copy().astype("float")
        return

    # compute weighted average, accumulate it and update the background
    cv2.accumulateWeighted(image, bg, aWeight)

# https://gogul09.github.io/software/hand-gesture-recognition-p1
# https://github.com/Gogul09/gesture-recognition/blob/master/part1.py



#-------------------------------------------------------------------------------
# Function - To segment the region of hand in the image
#-------------------------------------------------------------------------------
def segment(image, threshold=25):
    global bg
    # find the absolute difference between background and current frame
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # threshold the diff image so that we get the foreground
    thresholded = cv2.threshold(diff,
                                threshold,
                                255,
                                cv2.THRESH_BINARY)[1]

    # get the contours in the thresholded image
    (_, cnts, _) = cv2.findContours(thresholded.copy(),
                                    cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

    # return None, if no contours detected
    if len(cnts) == 0:
        return
    else:
        # based on contour area, get the maximum contour which is the hand
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)

# https://gogul09.github.io/software/hand-gesture-recognition-p1
# https://github.com/Gogul09/gesture-recognition/blob/master/part1.py




def hand_gesture_recognition(IP, PORT):
	 # initialize weight for running average
	aWeight = 0.5

	# get the reference to the webcam
	#camera = cv2.VideoCapture(0)

	# region of interest (ROI) coordinates
	top, right, bottom, left = 10, 350, 225, 590

	# initialize num of frames
	num_frames = 0

	#i=getframe(IP,PORT)
	#showimage(i)


	# keep looping, until interrupted
	while(True):
		
		# get frame
		frame=getframe(IP,PORT)
		# flip the frame so that it is not the mirror view
		frame = cv2.flip(frame, 1)

		# clone the frame
		clone = frame.copy()


		# convert the roi to grayscale and blur it
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (7, 7), 0)

		showimage(gray)


		# to get the background, keep looking till a threshold is reached
		# so that our running average model gets calibrated
		if num_frames < 30:
			run_avg(gray, aWeight)
	        else:
        		# segment the hand region
			hand = segment(gray)

			# check whether hand region is segmented
			if hand is not None:
				# if yes, unpack the thresholded image and
				# segmented region
				(thresholded, segmented) = hand

				# draw the segmented region and display the frame
				cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
				cv2.imshow("Thesholded", thresholded)

		# draw the segmented hand
		cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)

		##testing
		#	break


# https://gogul09.github.io/software/hand-gesture-recognition-p1
# https://github.com/Gogul09/gesture-recognition/blob/master/part1.py



