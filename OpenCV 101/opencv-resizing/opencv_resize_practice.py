# USAGE
# python opemcv_resize_practice.py

# import the necessary packages
import argparse
import re
import cv2
import imutils

# construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="Linkedin-Logo.png",
    help="path to the input image")
args = vars(ap.parse_args())

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# let's resize our image to be 150 pixels wide, but in order to prevent
# our resized image from being skewed/distorded, we must first calculate
# the ratio of the *new* width to the *old* width
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized)

# let's reisze the image to have a width of 50 pixels, again keeping
# in mind the aspect ratio
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (height)", resized)
cv2.waitKey(0)

# calculating the ratio each and every time we want to resize an
# image is as real pain, so let's use the imutils conveience function
# which will *automatically* maintain our aspect ratio for us
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)

# construct the list of interpolation methids in OpenCV
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4),
]

# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by 3x using the current interpolation mehod
    print("INFO {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
    
