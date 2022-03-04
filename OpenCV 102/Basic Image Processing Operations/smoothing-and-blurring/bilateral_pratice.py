# USAGE
# python image_drawing_practice.py

# import the necessary packages
import argparse
import cv2

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="cris.jpg",
    help="path to the input image")
args = vars(ap.parse_args())

# load the image and display it to our screen, and construct a list of 
# bilateral filtering parameters that are going to explore
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
params = [(13, 11, 11), (12, 21, 21), (13, 31, 31)]

# loop over the diameter, sigma color and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
    # apply bilateral; filtering to the image using the current set of 
    # parameters
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    
    # show the output image and associated parameters
    title = "Blurred d={}, sc={}, ss={}".format(
        diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
    
