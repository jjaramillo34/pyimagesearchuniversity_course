#USAGE
#python opencv_getting_setting.py

#import the necessary packages
import argparse
import cv2
from numpy import imag

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
    help="path to the input image")
args = vars(ap.parse_args())

# load the image, grab its spatial dimensions(width and height),
# and then display the original image to our screen
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# images are simply NumPy arrays -- with the origin (0,0) located at
# the top-left of the image
(b, g, r) = image[0,0]
print("Pixels at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print("Pixels at (50,50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel located at x=50, y=20
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20,50]
print("Pixels at (50,20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w// 2, h // 2)

# since we are using Numpy arrays, we can apply array slicing to grab
# large chucks/ regions of interest from the image -- here we grab the
# to-left corner of the image
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# in similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display to our screen
tr = image[0:cY, cX:w]
bl = image[cY:h, 0:cX]
br = image[cY:h, cX:w]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Left Corner", bl)
cv2.imshow("Bottom-Right Corner", br)

#set the top-left corner of the original image to be green
image[0:cY, 0:cX] = (0, 255, 0)

#show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)



