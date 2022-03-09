# USAGE
# python opencv_masking_practice.py

# import the necessary packages
import argparse
import cv2
import numpy as np

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
    help="path to the input image")
args = vars(ap.parse_args())

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# a mask is the same size as our image, but has only two pixels values, 0 to 255
# -- pixels with value of 0 (background) are ignored in the original image while
# mask pixels with a value 255 (foreground) are allowed to be kept
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Rectagular Mask", mask)

# apply our -- mask how only the person in the is cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)

# now let's make a circular mask with a radius of 100 pixels and appy the mask 
# again
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

# show th eoutput images
cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to image", masked)
cv2.waitKey(0)