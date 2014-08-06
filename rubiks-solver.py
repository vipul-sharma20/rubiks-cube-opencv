import numpy as np
import os
import cv2
from cv2 import *
import sys
import time
import json
def extract(imageName, face):
	im = cv2.imread(imageName)
	width, height = im.shape[:2]
	print width, height
	#im = cv2.equalizeHist(im)
	#kernel = np.ones((5,5),np.float32)/25
	#dst = cv2.filter2D(im,-1,kernel)
	#im = cv2.GaussianBlur(im,(5,5),100)
	im = cv2.bilateralFilter(im,9,75,75)
	#im = cv2.blur(im,(5,5))
	im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,24)

	#im = cv2.medianBlur(im,7)
	#cam = cv2.VideoCapture(0)
	#s, im = cam.read()

	position = {}
	#s, im = cam.read()
	hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)	# HSV image

	#lower_white = np.array([70,70,190], dtype=np.uint8)
	#upper_white = np.array([150,130,250], dtype=np.uint8)
	lower_white = np.array([70,20,130], dtype=np.uint8)
	upper_white = np.array([180,110,255], dtype=np.uint8)
	
	frame_threshed1 = cv2.inRange(hsv_img, lower_white, upper_white)
	imgray1 = frame_threshed1
	cv2.imshow('white', frame_threshed1)
	ret,thresh1 = cv2.threshold(frame_threshed1,127,255,0)

	contours1, hierarchy1 = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	areas = [cv2.contourArea(c) for c in contours1]
	for elem in range(len(areas)):
		areas[elem] = int(areas[elem])
		print areas[elem]
	max_area = 0
	print '-'*50
	for elem in areas:
		if elem > max_area:
			max_area = elem
	#print max_index
	get = []
	#max_area = areas[max_index]
	for a in range(len(areas)):
		#print areas[a] - max_area
		if areas[a] - max_area in range(-1000, 1000) and areas[a] >= 1500:
			print areas[a]
			get.append(contours1[a])
		else:
			pass
	#cnt=contours1[max_index]
		
	for elem in get:
		for t in elem:

			x,y,w,h = cv2.boundingRect(elem)
			#print x,
			#print y
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			centroid_x = (x + x+w)/2
			centroid_y = (y + y+h)/2
			if centroid_x > 0 and centroid_x < 66:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'1'] = 'white'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'4'] = 'white'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'7'] = 'white'
			if centroid_x > 66 and centroid_x < 133:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'2'] = 'white'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'5'] = 'white'
				elif centroid_y > 133 and centroid_y < 200:
					#position['white'].append(face+'8')
					position[face+'8'] = 'white'
			if centroid_x > 133	 and centroid_x < 200:
				if centroid_y > 0 and centroid_y < 66:
					#position['white'].append(face+'3')
					position[face+'3'] = 'white'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'6'] = 'white'
				elif centroid_y > 133 and centroid_y < 200:
					#position['white'].append(face+'9')
					position[face+'9'] = 'white'		
			cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)
	"""for cnt in contours1:
		x,y,w,h = cv2.boundingRect(cnt)
		#print x,
		#print y
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)"""

	#print '------------------------'

	#COLOR_MIN = np.array([15, 90, 130],np.uint8)		# HSV color code lower and upper bounds
	#COLOR_MAX = np.array([50, 160, 200],np.uint8)		# color yellow 

	COLOR_MIN = np.array([15, 90, 130],np.uint8)		# HSV color code lower and upper bounds
	COLOR_MAX = np.array([60, 245, 245],np.uint8)		# color yellow 
	
	frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)		# Thresholding image
	imgray = frame_threshed

	ret,thresh = cv2.threshold(frame_threshed,127,255,cv2.THRESH_BINARY)
	#thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	#            cv2.THRESH_BINARY,11,2)
	cv2.imshow('yellow', thresh)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	areas = [cv2.contourArea(c) for c in contours]
	for elem in range(len(areas)):
		areas[elem] = int(areas[elem])
		print areas[elem]
	max_area = 0
	print '-'*50
	for elem in areas:
		if elem > max_area:
			max_area = elem
	#print max_index
	get = []
	#max_area = areas[max_index]
	for a in range(len(areas)):
		
		if areas[a] - max_area in range(-1000, 1000) and areas[a] >= 1500:
			print areas[a]	
			get.append(contours[a])
			

		else:
			pass
	#cnt=contours1[max_index]
	for elem in get:
		for t in elem:
			#print 'hey'
			x,y,w,h = cv2.boundingRect(elem)
			#print x,
			#print y
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			centroid_x = (x + x+w)/2
			centroid_y = (y + y+h)/2
			cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)
			if centroid_x > 0 and centroid_x < 66:
				if centroid_y > 0 and centroid_y < 66:
					position[face+'1'] = 'yellow'

				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'4'] = 'yellow'
				elif centroid_y > 133 and centroid_y < 200:

					position[face+'7'] = 'yellow'
			if centroid_x > 66 and centroid_x < 133:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'2'] = 'yellow'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'5'] = 'yellow'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'8'] = 'yellow'
			if centroid_x > 133	 and centroid_x < 200:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'3'] = 'yellow'
				elif centroid_y > 66 and centroid_y < 133:
					position[face+'6'] = 'yellow'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'9'] = 'yellow'	

	print type(contours)
	"""for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		#print x,
		#print y
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2
		cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)"""


	#lower_blue = np.array([80,180,140], dtype=np.uint8)
	#upper_blue = np.array([140,245,205], dtype=np.uint8)

	lower_blue = np.array([80,180,190], dtype=np.uint8)
	upper_blue = np.array([120,255,255], dtype=np.uint8)

	frame_threshed3 = cv2.inRange(hsv_img, lower_blue, upper_blue)		# Thresholding image
	imgray3 = frame_threshed3
	ret,thresh3 = cv2.threshold(frame_threshed3,127,255,3)

	cv2.imshow('blue', frame_threshed3)

	contours3, hierarchy3 = cv2.findContours(thresh3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	areas = [cv2.contourArea(c) for c in contours3]
	for elem in range(len(areas)):
		areas[elem] = int(areas[elem])
		#print areas[elem]
	max_area = 0
	for elem in areas:
		if elem > max_area:
			max_area = elem
	#print max_index
	get = []
	print '-'*50
	for a in range(len(areas)):
		#print areas[a] - max_area
		if areas[a] - max_area in range(-1200, 1200) and areas[a] >= 1500:
			#print areas[a]
			get.append(contours3[a])
		else:
			pass
	#cnt=contours1[max_index]
	for elem in get:
		for t in elem:
			x,y,w,h = cv2.boundingRect(elem)
			#print x,
			#print y
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			centroid_x = (x + x+w)/2
			centroid_y = (y + y+h)/2
			cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)
			if centroid_x > 0 and centroid_x < 66:
				if centroid_y > 0 and centroid_y < 66:
					position[face+'1'] = 'blue'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'4'] = 'blue'
				elif centroid_y > 133 and centroid_y < 200:

					position[face+'7'] = 'blue'
			if centroid_x > 66 and centroid_x < 133:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'2'] = 'blue'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'5'] = 'blue'
				elif centroid_y > 133 and centroid_y < 200:
					position[face+'8'] = 'blue'
			if centroid_x > 133	 and centroid_x < 200:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'3'] = 'blue'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'6'] = 'blue'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'9'] = 'blue'	

	"""for cnt in contours3:
		x,y,w,h = cv2.boundingRect(cnt)
		#print x,
		#print y
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2
		cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)"""


	#lower_orange = np.array([0, 130, 90],np.uint8)		# HSV color code lower and upper bounds
	#upper_orange = np.array([20, 210, 170],np.uint8)		# color orange
	lower_orange = np.array([5, 150, 150],np.uint8)		# HSV color code lower and upper bounds
	upper_orange = np.array([15, 235, 250],np.uint8)		# color orange

	frame_threshed2 = cv2.inRange(hsv_img, lower_orange, upper_orange)		# Thresholding image
	imgray2 = frame_threshed2
	ret,thresh2 = cv2.threshold(frame_threshed2,127,255,2)
	cv2.imshow('Orange', frame_threshed2)
	contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	areas = [cv2.contourArea(c) for c in contours2]
	for elem in range(len(areas)):
		areas[elem] = int(areas[elem])
		#print areas[elem]
	max_area = 0
	for elem in areas:
		if elem > max_area:
			max_area = elem
	#print max_index
	get = []
	print '-'*50
	for a in range(len(areas)):
		if areas[a] - max_area in range(-1000, 1000) and areas[a] >= 1500:

			#print areas[a]
			get.append(contours2[a])
		else:
			pass
	#cnt=contours1[max_index]
	for elem in get:
		for t in elem:
			x,y,w,h = cv2.boundingRect(elem)
			#print x,
			#print y
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			centroid_x = (x + x+w)/2
			centroid_y = (y + y+h)/2
			cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)
			if centroid_x > 0 and centroid_x < 66:
				if centroid_y > 0 and centroid_y < 66:
					position[face+'1'] = 'orange'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'4'] = 'orange'
				elif centroid_y > 133 and centroid_y < 200:

					position[face+'7'] = 'orange'
			if centroid_x > 66 and centroid_x < 133:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'2'] = 'orange'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'5'] = 'orange'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'8'] = 'orange'
			if centroid_x > 133	 and centroid_x < 200:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'3'] = 'orange'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'6'] = 'orange'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'9'] = 'orange'	

	"""for cnt in contours2:
		x,y,w,h = cv2.boundingRect(cnt)
		#print x,
		#print y
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)"""

	#lower_green = np.array([60, 120, 80],np.uint8)		# HSV color code lower and upper bounds
	#upper_green = np.array([100, 170, 120],np.uint8)		# color orange
	lower_green = np.array([60, 110, 110],np.uint8)		# HSV color code lower and upper bounds
	upper_green = np.array([100, 220, 250],np.uint8)		# color orange
	

	frame_threshed4 = cv2.inRange(hsv_img, lower_green, upper_green)		# Thresholding image
	imgray4 = frame_threshed4
	ret,thresh4 = cv2.threshold(frame_threshed4,127,255,0)
	cv2.imshow('green', frame_threshed4)
	contours4, hierarchy4 = cv2.findContours(thresh4,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	areas = [cv2.contourArea(c) for c in contours4]
	for elem in range(len(areas)):
		areas[elem] = int(areas[elem])
		#print areas[elem]
	max_area = 0
	for elem in areas:
		if elem > max_area:
			max_area = elem
	#print max_index
	get = []
	#max_area = areas[max_index]
	for a in range(len(areas)):
		#print areas[a] - max_area
		if areas[a] - max_area in range(-1000, 1000) and areas[a] >= 1500:

			get.append(contours4[a])
		else:
			pass
	#cnt=contours1[max_index]
	for elem in get:
		for t in elem:
			x,y,w,h = cv2.boundingRect(elem)
			#print x,
			#print y
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			centroid_x = (x + x+w)/2
			centroid_y = (y + y+h)/2
			cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)
			if centroid_x > 0 and centroid_x < 66:
				if centroid_y > 0 and centroid_y < 66:
					position[face+'1'] = 'green'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'4'] = 'green'
				elif centroid_y > 133 and centroid_y < 200:

					position[face+'7'] = 'green'
			if centroid_x > 66 and centroid_x < 133:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'2'] = 'green'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'5'] = 'green'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'8'] = 'green'
			if centroid_x > 133	 and centroid_x < 200:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'3'] = 'green'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'6'] = 'green'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'9'] = 'green'	
	"""for cnt in contours4:
		x,y,w,h = cv2.boundingRect(cnt)
		#print x,
		#print y
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2
		cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)"""


	#lower_red = np.array([140, 120, 70],np.uint8)		# HSV color code lower and upper bounds
	#upper_red = np.array([210, 220, 170],np.uint8)		# color orange
	lower_red = np.array([120, 120, 140],np.uint8)		# HSV color code lower and upper bounds
	upper_red = np.array([180, 250, 200],np.uint8)		# color orange

	frame_threshed5 = cv2.inRange(hsv_img, lower_red, upper_red)		# Thresholding image
	imgray5 = frame_threshed5
	ret,thresh5 = cv2.threshold(frame_threshed5,127,255,0)
	cv2.imshow('red', frame_threshed5)
	contours5, hierarchy5 = cv2.findContours(thresh5,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	areas = [cv2.contourArea(c) for c in contours5]
	for elem in range(len(areas)):
		areas[elem] = int(areas[elem])
		#print areas[elem]
	max_area = 0
	for elem in areas:
		if elem > max_area:
			max_area = elem
	#print max_index
	get = []
	#max_area = areas[max_index]
	for a in range(len(areas)):
		if areas[a] - max_area in range(-1500, 1500) and areas[a] >= 1500:
			print areas[a]

			get.append(contours5[a])
		else:
			pass
	#cnt=contours1[max_index]
	for elem in get:
		for t in elem:
			x,y,w,h = cv2.boundingRect(elem)
			#print x,
			#print y
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			centroid_x = (x + x+w)/2
			centroid_y = (y + y+h)/2
			cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)
			if centroid_x > 0 and centroid_x < 66:
				if centroid_y > 0 and centroid_y < 66:
					position[face+'1'] = 'red'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'4'] = 'red'
				elif centroid_y > 133 and centroid_y < 200:

					position[face+'7'] = 'red'
			if centroid_x > 66 and centroid_x < 133:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'2'] = 'red'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'5'] = 'red'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'8'] = 'red'
			if centroid_x > 133	 and centroid_x < 200:
				if centroid_y > 0 and centroid_y < 66:
					
					position[face+'3'] = 'red'
				elif centroid_y > 66 and centroid_y < 133:
					
					position[face+'6'] = 'red'
				elif centroid_y > 133 and centroid_y < 200:
					
					position[face+'9'] = 'red'	

	"""for cnt in contours5:
		x,y,w,h = cv2.boundingRect(cnt)
		#print x,
		#print y
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2
		cv2.circle(im, (centroid_x, centroid_y), 2, (255,0,0), 2)"""


	

	cv2.line(im,(0,66),(200,66),(255,0,0),2)
	cv2.line(im,(0,133),(200,133),(255,0,0),2)
	cv2.line(im,(66,0),(66,200),(255,0,0),2)
	cv2.line(im,(133,0),(133,200),(255,0,0),2)
	#cv2.imshow("Show",im)
	cv2.imshow(imageName, im)
	cv2.imwrite(imageName+'_extracted.jpg', im)
	return position, im 
	cv2.waitKey()
	cv2.destroyAllWindows()

def captureImage(imageName):

	timeout = 15
	first_time = time.time()
	last_time = first_time

	cam = cv2.VideoCapture(0)
	winName = "Smile :D"
	winName1 = "cropped"
	cv2.namedWindow(winName1, cv2.CV_WINDOW_AUTOSIZE)
	cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
	print 'READY !! '
	s = True
	while s:
	    s, im = cam.read()
	    cv2.rectangle(im,(300,300),(100,100),(0,255,0),3)
	    cv2.imshow(winName, im)
	    #if cv2.waitKey(33) == ord('a'):
	    #print "pressed a"
	    #cv2.imwrite("captured.png", im)
	    #img = cv2.imread("captured.jpg")
	    #img = cv2.imread("captured.png")
	    #cv2.imshow(winName1, img)
	    #print type(im)
	    crop_img = im[100:300, 100:300] # Crop from x, y, w, h -> 100, 200, 300, 400
	    cv2.imshow(winName1, crop_img)
	    #cv2.imwrite("cropped.jpg", crop_img)
	    #print type(crop_img)
	    new_time = time.time()
	    if  new_time - last_time > timeout:
	        last_time = new_time
	        print "Its been %f seconds" % (new_time - first_time)
	        cv2.imwrite(imageName, crop_img)
	        break

	    key = cv2.waitKey(10)
	    if key == 27:
	       print 'done'
	    
	       cv2.destroyWindow(winName)
	       break
	    	#sys.exit(0)

def main():
	#captureImage(imageName='front_face.bmp')
	#captureImage(imageName='right_face.bmp')
	#captureImage(imageName='back_face.bmp')
	#captureImage(imageName='left_face.bmp')
	#captureImage(imageName='top_face.bmp')
	#captureImage(imageName='bottom_face.bmp')
	front,s = extract(imageName='front_face.bmp', face='f')
	right,s = extract(imageName='right_face.bmp', face='r')
	back,s = extract(imageName='back_face.bmp', face='b')
	left,s = extract(imageName='left_face.bmp', face='l')
	top,s = extract(imageName='top_face.bmp', face='t')
	bottom,s = extract(imageName='bottom_face.bmp', face='bo')
	#bottom['bo7'] = 'orange'

	print json.dumps(front, indent=2)
	print json.dumps(left, indent=2)
	print json.dumps(right, indent=2)
	print json.dumps(back, indent=2)
	print json.dumps(top, indent=2)
	print json.dumps(bottom, indent=2)

	corners = dict()
	edges = dict()
	
	corners['c1'] = []
	corners['c2'] = []
	corners['c3'] = []
	corners['c4'] = []
	corners['c5'] = []
	corners['c6'] = []
	corners['c7'] = []
	corners['c8'] = []
	temp = {}
	temp_edge = {}
	solved_state = {0:'orange', 1:'blue', 2:'orange', 3:'yellow', 4:'orange', 5:'green', 6:'orange', 7:'white', 8:'red',
		   9:'blue', 10:'red',11:'yellow', 12:'red', 13:'green', 14:'red', 15:'white', 16:'blue', 17:'yellow',
		   18:'blue', 19:'white', 20:'green', 21:'yellow', 22:'green', 23:'white', 24:'orange', 25:'blue',
		   26:'yellow', 27:'orange', 28:'yellow', 29:'green', 30:'orange', 31:'green', 32:'white', 33:'orange',
		   34:'white', 35:'blue', 36:'red', 37:'yellow', 38:'blue', 39:'red', 40:'blue', 41:'white', 42:'red',
		   43:'white', 44:'green', 45:'red', 46:'green', 47:'yellow'}


	build_corners(corners, 'c1', front['f1'])
	build_corners(corners, 'c1', top['t7'])
	build_corners(corners, 'c1', left['l3'])
	temp['c1'] = ['F', 'U', 'L']

	build_corners(corners, 'c2', front['f3'])
	build_corners(corners, 'c2', top['t9'])
	build_corners(corners, 'c2', right['r1'])
	temp['c2'] = ['F', 'U', 'R']

	build_corners(corners, 'c3', right['r3'])
	build_corners(corners, 'c3', top['t3'])
	build_corners(corners, 'c3', back['b1'])
	temp['c3'] = ['R', 'U', 'B']

	build_corners(corners, 'c4', back['b3'])
	build_corners(corners, 'c4', top['t1'])
	build_corners(corners, 'c4', left['l1'])
	temp['c4'] = ['B', 'U', 'L']

	build_corners(corners, 'c5', front['f7'])
	build_corners(corners, 'c5', bottom['bo1'])
	build_corners(corners, 'c5', left['l9'])
	temp['c5'] = ['F', 'D', 'L']

	build_corners(corners, 'c6', front['f9'])
	build_corners(corners, 'c6', bottom['bo3'])
	build_corners(corners, 'c6', right['r7'])
	temp['c6'] = ['F', 'D', 'R']

	build_corners(corners, 'c7', right['r9'])
	build_corners(corners, 'c7', bottom['bo9'])
	build_corners(corners, 'c7', back['b7'])
	temp['c7'] = ['R', 'D', 'B']

	build_corners(corners, 'c8', back['b9'])
	build_corners(corners, 'c8', bottom['bo7'])
	build_corners(corners, 'c8', left['l7'])
	temp['c8'] = ['B', 'D', 'L']

	edges['e1'] = []
	edges['e2'] = []
	edges['e3'] = []
	edges['e4'] = []
	edges['e5'] = []
	edges['e6'] = []
	edges['e7'] = []
	edges['e8'] = []
	edges['e9'] = []
	edges['e10'] = []
	edges['e11'] = []
	edges['e12'] = []

	edges['e1'].append(front['f2'])
	edges['e1'].append(top['t8'])
	temp_edge['e1'] = ['F', 'U']

	edges['e2'].append(right['r2'])
	edges['e2'].append(top['t6'])
	temp_edge['e2'] = ['R', 'U']	

	edges['e3'].append(back['b2'])
	edges['e3'].append(top['t2'])
	temp_edge['e3'] = ['B', 'U']

	edges['e4'].append(left['l2'])
	edges['e4'].append(top['t4'])
	temp_edge['e4'] = ['L', 'U']

	edges['e5'].append(front['f8'])
	edges['e5'].append(bottom['bo2'])
	temp_edge['e5'] = ['F', 'D']

	edges['e6'].append(right['r8'])
	edges['e6'].append(bottom['bo6'])
	temp_edge['e6'] = ['R', 'D']

	edges['e7'].append(back['b8'])
	edges['e7'].append(bottom['bo8'])
	temp_edge['e7'] = ['B', 'D']

	edges['e8'].append(left['l8'])
	edges['e8'].append(bottom['bo4'])
	temp_edge['e8'] = ['L', 'D']

	edges['e9'].append(front['f6'])
	edges['e9'].append(right['r4'])
	temp_edge['e9'] = ['F', 'R']	

	edges['e10'].append(right['r6'])
	edges['e10'].append(back['b4'])
	temp_edge['e10'] = ['R', 'B']

	edges['e11'].append(back['b6'])
	edges['e11'].append(left['l4'])
	temp_edge['e11'] = ['B', 'L']

	edges['e12'].append(left['l6'])
	edges['e12'].append(front['f4'])
	temp_edge['e12'] = ['L', 'F']
	print temp_edge
	cube = dict()
	position = dict()
	p = {'e1':'F', 'e2':'R', 'e3':'B', 'e4':'L', 'e5':'F', 'e6':'R', 'e7':'B', 'e8':'L', 'e9':'F', 'e10':'L', 'e11':'B', 'e12':'L'}

	for pos, color in edges.iteritems():
		
		if set(color) == set(['yellow', 'orange']):
			for i in range(len(color)):
				if color[i] == 'yellow':
					position['3'] = temp_edge[pos][i]
				else:
					position['2'] = temp_edge[pos][i]

#-----------------------------------------------------------------------------------------------

		elif set(color) == set(['orange', 'blue']):
			for i in range(len(color)):
				if color[i] == 'orange':
					position['0'] = temp_edge[pos][i]
				else:
					position['1'] = temp_edge[pos][i]


#-------------------------------------------------------------------------------------------------

		elif set(color) == set(['orange','green']):
			for i in range(len(color)):
				if color[i] == 'orange':
					position['4'] = temp_edge[pos][i]
				else:
					position['5'] = temp_edge[pos][i]


#---------------------------------------------------------------------------------------------------

		elif set(color) == set(['orange', 'white']):
			for i in range(len(color)):
				if color[i] == 'orange':
					position['6'] = temp_edge[pos][i]
				else:
					position['7'] = temp_edge[pos][i]
	
 
 #---------------------------------------------------------------------------------------------------

		elif set(color) == set(['red', 'blue']):
			for i in range(len(color)):
				if color[i] == 'red':
					position['8'] = temp_edge[pos][i]
				else:
					position['9'] = temp_edge[pos][i]

#-----------------------------------------------------------------------------------------------------

		elif set(color) == set(['red', 'yellow']):
			for i in range(len(color)):

				if color[i] == 'red':
					position['10'] = temp_edge[pos][i]
				else:
					position['11'] = temp_edge[pos][i]

#-----------------------------------------------------------------------------------------------------------

		elif set(color) == set(['red', 'green']):
			for i in range(len(color)):
				if color[i] == 'red':
					position['12'] = temp_edge[pos][i]
				else:
					position['13'] = temp_edge[pos][i]	

#-------------------------------------------------------------------------------------------------------------

		elif set(color) == set(['red', 'white']):
			print 'here'
			for i in range(len(color)):
				if color[i] == 'red':
					position['14'] = temp_edge[pos][i]
				else:
					position['15'] = temp_edge[pos][i]	

#---------------------------------------------------------------------------------------------------------------

		elif set(color) == set(['blue', 'yellow']):
				for i in range(len(color)):
					if color[i] == 'blue':
						position['16'] = temp_edge[pos][i]
					else:
						position['17'] = temp_edge[pos][i]	

#---------------------------------------------------------------------------------------------------------------

		elif set(color) == set(['blue', 'white']):
			for i in range(len(color)):
				if color[i] == 'blue':
					position['18'] = temp_edge[pos][i]
				else:
					position['19'] = temp_edge[pos][i]

#------------------------------------------------------------------------------------------------------------------	

		elif set(color) == set(['green', 'yellow']):
			for i in range(len(color)):
				if color[i] == 'green':
					position['20'] = temp_edge[pos][i]
				else:
					position['21'] = temp_edge[pos][i]	

#------------------------------------------------------------------------------------------------------------------

		elif set(color) == set(['green', 'white']):
			for i in range(len(color)):
				if color[i] == 'green':
					position['22'] = temp_edge[pos][i]
				else:
					position['23'] = temp_edge[pos][i]
		else:
			print color[0], color[1], pos
			                   
	

#------------------------------------------------------------------------------------------------------------------
											# 	t		l	f
	for pos, corner in corners.iteritems(): # orange white blue 33 34 35
		
		if set(corner) == set(['orange', 'white', 'blue']):
			for i in range(len(corner)):
				if corner[i] == 'orange':
					position['33'] = temp[pos][i] 
				if corner[i] == 'white':
					position['34'] = temp[pos][i]
				if corner[i] == 'blue':
					position['35'] = temp[pos][i]


		elif set(corner) == set(['orange', 'blue', 'yellow']):
			for i in range(len(corner)):
				if corner[i] == 'orange':
					position['24'] = temp[pos][i] 
				if corner[i] == 'blue':
					position['25'] = temp[pos][i]
				if corner[i] == 'yellow':
					position['26'] = temp[pos][i]

		elif set(corner) == set(['orange', 'yellow', 'green']):
			for i in range(len(corner)):
				if corner[i] == 'orange':
					position['27'] = temp[pos][i] 
				if corner[i] == 'yellow':
					position['28'] = temp[pos][i]
				if corner[i] == 'green':
					position['29'] = temp[pos][i]

		if set(corner) == set(['orange', 'green','white']):
			for i in range(len(corner)):
				if corner[i] == 'orange':
					position['30'] = temp[pos][i] 
				if corner[i] == 'green':
					position['31'] = temp[pos][i]
				if corner[i] == 'white':
					position['32'] = temp[pos][i]


		if set(corner) == set(['red', 'yellow', 'blue']):
			for i in range(len(corner)):
				if corner[i] == 'red':
					position['36'] = temp[pos][i] 
				if corner[i] == 'yellow':
					position['37'] = temp[pos][i]
				if corner[i] == 'blue':
					position['38'] = temp[pos][i]

		if set(corner) == set(['red', 'blue', 'white']):
			for i in range(len(corner)):
				if corner[i] == 'red':
					position['39'] = temp[pos][i] 
				if corner[i] == 'blue':
					position['40'] = temp[pos][i]
				if corner[i] == 'white':
					position['41'] = temp[pos][i]
			
		if set(corner) == set(['red', 'white', 'green']):
			for i in range(len(corner)):
				if corner[i] == 'red':
					position['42'] = temp[pos][i] 
				if corner[i] == 'white':
					position['43'] = temp[pos][i]
				if corner[i] == 'green':
					position['44'] = temp[pos][i]

		if set(corner) == set(['red', 'green', 'yellow']):
			for i in range(len(corner)):
				if corner[i] == 'red':
					position['45'] = temp[pos][i] 
				if corner[i] == 'green':
					position['46'] = temp[pos][i]
				if corner[i] == 'yellow':
					position['47'] = temp[pos][i]

	print corners
	print position
	print position['42']
	print temp
	solution(position)

def build_corners(corners, c_no, data):
	corners[c_no].append(data)

def solution(position):
	pos = ''
	a = 0
	while a <= 22:
		pos = pos + position[str(a)] + position[str(a+1)] + ' '
		a += 2

	a = 24
	while a <= 46:
		pos = pos + position[str(a)] + position[str(a+1)] + position[str(a+2)] + ' '
		a += 3
	t = open('in.dat', 'w')
	t.write(pos.strip())
	t.close()
	os.system("python solver.py < in.dat > result.txt")
	t = open('result.txt', 'rb')
	p = t.read()
	#print p
	
	#p = p.replace('\n', '')
	print pos.strip()
	print p
	
	do = ''
	move = 0
	while move < len(p):
		do = do + p[move] + p[move+1] + ' '
		move += 2
	#print do

	
	"""change = {}
	change['F'] = {}
	change['B'] = {}
	change['R'] = {}
	change['L'] = {}
	change['U'] = {}
	change['D'] = {}

	change['F']['90'] = {}
	#change['F']['90'] = {}
	change['F']['90']['U'] = 'R'
	change['F']['90']['R'] = 'D'
	change['F']['90']['D'] = 'L'
	change['F']['90']['L'] = 'U'

	change['F']['180'] = {}
	change['F']['180']['U'] = 'D'
	change['F']['180']['R'] = 'L'
	change['F']['180']['D'] = 'U'
	change['F']['180']['L'] = 'R'

        change['F']['270'] = {} 
        change['F']['270']['U'] = 'L'   
        change['F']['270']['R'] = 'U'   
        change['F']['270']['D'] = 'R'
        change['F']['270']['L'] = 'D'

        change['B']['180'] = {} 
        change['B']['180']['U'] = 'D'   
        change['B']['180']['R'] = 'L'   
        change['B']['180']['D'] = 'U'
        change['B']['180']['L'] = 'R'

        change['B']['90'] = {}
        change['B']['90']['U'] = 'L'
        change['B']['90']['R'] = 'U'
        change['B']['90']['D'] = 'R'
        change['B']['90']['L'] = 'D'

	change['B']['270'] = {}
        change['B']['270']['U'] = 'R'
        change['B']['270']['R'] = 'D'
        change['B']['270']['D'] = 'L'
        change['B']['270']['L'] = 'U'

	change['U']['90'] = {}
        change['U']['90']['F'] = 'L'
        change['U']['90']['L'] = 'B'
        change['U']['90']['B'] = 'R'
        change['U']['90']['R'] = 'F'

        change['U']['180'] = {}
        change['U']['180']['F'] = 'B'
        change['U']['180']['L'] = 'R'
        change['U']['180']['B'] = 'F'
        change['U']['180']['R'] = 'L'

        change['U']['270'] = {}
        change['U']['270']['F'] = 'R'
        change['U']['270']['L'] = 'F'
        change['U']['270']['B'] = 'L'
        change['U']['270']['R'] = 'B'

        change['D']['90'] = {}
        change['D']['90']['F'] = 'R'
        change['D']['90']['L'] = 'F'
        change['D']['90']['B'] = 'L'
        change['D']['90']['R'] = 'B'

        change['D']['180'] = {}
        change['D']['180']['F'] = 'B'
        change['D']['180']['L'] = 'R'
        change['D']['180']['B'] = 'F'
        change['D']['180']['R'] = 'L'

	change['D']['270'] = {}
        change['D']['270']['F'] = 'L'
        change['D']['270']['L'] = 'B'
        change['D']['270']['B'] = 'R'
        change['D']['270']['R'] = 'F'

	change['R']['90'] = {}
	change['R']['90']['U'] = 'B'
	change['R']['90']['B'] = 'D'
	change['R']['90']['D'] = 'F'
	change['R']['90']['F'] = 'U'

	change['R']['180'] = {}
	change['R']['180']['U'] = 'D'
	change['R']['180']['B'] = 'F'
	change['R']['180']['D'] = 'U'
	change['R']['180']['F'] = 'B'

	change['R']['270'] = {}
	change['R']['270']['U'] = 'F'
	change['R']['270']['B'] = 'U'
	change['R']['270']['D'] = 'B'
	change['R']['270']['F'] = 'D'

	change['L']['90'] = {}
	change['L']['90']['U'] = 'F'
        change['L']['90']['F'] = 'D'
        change['L']['90']['D'] = 'B'
        change['L']['90']['B'] = 'U'

        change['L']['180'] = {}
        change['L']['180']['U'] = 'D'
        change['L']['180']['F'] = 'B'
        change['L']['180']['D'] = 'U'
        change['L']['180']['B'] = 'F'

	change['L']['270'] = {}
	change['L']['270']['U'] = 'B' 
        change['L']['270']['F'] = 'U'
        change['L']['270']['D'] = 'F'
        change['L']['270']['B'] = 'D'
	
	print change
	print do.split(' ')
	rotation = pos.split(' ')
	after = list(pos)
	
	face_front = [['U','F'], ['R','F'], ['D','F'], ['L','F'], ['U','L','F'], ['U','R','F'], ['D','R','F'], ['D','L','F']]	
	face_right = [['U','R'], ['B','R'], ['D','R'], ['R','F'], ['U','R','F'], ['R','B','U'], ['D','R','B'], ['D','R','F']]
	face_back =  [['U','B'], ['B','L'], ['B','D'], ['B','R'], ['U','R','B'], ['U','L','B'], ['B','D','L'], ['B','D','R']]
	face_left =  [['L','U'], ['L','B'], ['L','D'], ['L','F'], ['L','B','U'], ['L','B','D'], ['L','F','U'], ['L','F','D']]
	face_up   =  [['U','F'], ['U','R'], ['U','B'], ['U','L'], ['U','F','R'], ['U','F','L'], ['U','R','B'], ['U','L','B']]
	face_down =  [['D','F'], ['D','R'], ['D','B'], ['D','L'], ['D','F','R'], ['D','R','B'], ['D','L','B'], ['D','L','F']]
	
	for elem in do.strip().split(' '):
		if elem == '':
			break
		first = elem[0]
		
		second = ''
		new_pos = {}
		if elem[1] == '1':
			second = '90'
		elif elem[1] == 2:
			second = '180'
		elif elem[1] == '270':
			second = '270'
		else:
			print 'something went wrong'
		if first == 'L':
			to_do = face_left
		elif first == 'R':
			to_do = face_right
		elif first == 'F':
			to_do = face_front
		elif first == 'D':
			to_do = face_down
		elif first == 'U':
			to_do = face_up
		else: 
			print 'something wen wrong'

		for x,y in change[first][second].iteritems():
			new_pos[x] = y
		
		print 'new pos: ',
		print new_pos
		count = 0
		#print len(pos)
		p_count = 0 
		for p in rotation:
			#print count
			senti = False
			for elem in to_do:
				if set(elem) == set(list(p)):
					senti = True
			if senti:
				for x in list(p):
					if after[count] == ' ':
						count += 1
					if x in new_pos:

						after[count] = str(new_pos[x])
						count += 1
			else:
				for x in list(p):
					if after[count] == ' ':
						count += 1
					else:
						after[count] = x
						count += 1
			p_count += 1
		print ''.join(after)"""
								
main()
