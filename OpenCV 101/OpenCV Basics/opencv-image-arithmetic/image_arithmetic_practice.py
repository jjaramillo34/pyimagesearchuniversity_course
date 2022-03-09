# USAGE
# python image_arithmetic_practice.py

# import the necessary packages
import argparse
import cv2
import numpy as np

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="Linkedin-Logo.png",
    help="path to the input image")
args = vars(ap.parse_args())

# iamges are Numpy arrays stored as unsigned 8-bit integers (uint8) with values
# in the range [0, 255]; when using the substract functions in OpenCv, these 
# values will be *clipped* to this range, even if they outside the range[0, 255]
# after applying the operation
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("max of 255: {}".format(added))
print("min of 0: {}".format(subtracted))

# using Numpy arithmetic operations (rather the OpenCV operations) will result
# in a modulo ("wrap around") instead of being clipped to the range [0, 255]
added = np.uint8([200]) + np.uint8([100])
subtracted = np.uint8([50]) - np.uint8([100])
print("wrap around: {}".format(added))
print("wrap around: {}".format(subtracted))

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# increasing the pixel intensities in our input image by 100 is accomplished 
# by constructiong a NumPy array that has the *same dimensions* as out input 
# image, filling it with ones, multiplying it by 100, and then adding the image 
# and matrix together
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Ligher", added)

# similarly, we can substract 50 from all pixels in our image and it darker
M = np.ones(image.shape, dtype="uint8")
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)
cv2.waitKey(0)

