#!/usr/local/bin/python

import cv, cv2
import numpy as np
from matplotlib import pyplot as plt
import Image
from flask import Flask

# # Display image to see
# img = cv.LoadImage('picture.jpg')
# cv.NamedWindow("Example", cv.CV_WINDOW_AUTOSIZE )
# cv.ShowImage("Example", img )
# cv.WaitKey(1000)
# cv.DestroyWindow("Example")


# Work with the "image" variable for the rest
image = cv2.imread('rainbow.jpg')

#get color coordinates from picture
#let's say rgb (r,g,b)

# define the list of boundaries
# boundaries = [
# 	([17, 15, 100], [50, 56, 200]),			#red/maroon
# 	([86, 31, 4], [220, 88, 50]),			#blue
# 	([25, 146, 190], [62, 174, 250]),		#orange/yellow/pink
# 	([103, 86, 65], [145, 133, 128])		#grey
# ]

print request.GET['panel']

red = [([103, 86, 65], [145, 133, 128])]
blue = [([86, 31, 4], [220, 88, 50])]
grey = [([103, 86, 65], [145, 133, 128])]
orange = ([25, 146, 190], [62, 174, 250])

im = Image.open('rainbow.jpg')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((x, y))				#we need x and y from javascript

if (4 <= r <= 50 & 31 <=g<=88 & 86<=220):		#green?
	for (lower, upper) in green:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
	 
		# show the images
		cv2.imshow("images", np.hstack([image, output]))
		cv2.waitKey(1000)
		

if (65 <= r <= 128 & 86 <=g<=133 & 103<=145):			#red
	# loop over the boundaries
	for (lower, upper) in red:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
	 
		# show the images
		cv2.imshow("images", np.hstack([image, output]))
		cv2.waitKey(1000)


	crop_img = image[:, 100:300]
	cv2.imshow("cropped", crop_img)
	cv2.waitKey(0)







