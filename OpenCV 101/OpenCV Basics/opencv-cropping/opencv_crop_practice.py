# USAGE
# python image_drawing_practice.py

# import the necessary packages
import argparse
import cv2

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
    help="path to the input image")
args = vars(ap.parse_args())

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# cropping an image with OpenCV is accomplished via simple Numpy array slices
# is startY:endY, startX:startX -- here we are cropping the face from the 
# image (these coordinates were determined using photo editing software as
# Photoshop, GIMP, Paint, etc.)
face = image[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey(0)

# apply another image crop, this time extracting the body
body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)

# apply another image crop, this time extracting group people
group = image[89:240, 0:77]
cv2.imshow("Group", group)
cv2.waitKey(0)
