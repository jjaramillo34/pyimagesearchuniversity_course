# USAGE
# python opencv_rotate_practice.py

# import the necessary packages
import argparse
import cv2
import imutils

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="Linkedin-Logo.png",
    help="path to the input image")
args = vars(ap.parse_args())

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

#rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)

#rotate our image by -90 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 90 degrees", rotated)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)

# use our imutils function to raote an image 180 degrees
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)

# rotate our image by 33 degrees counterclockwise, ensuring the
# entire rotated image still views in the viewing area
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated without Cropping", rotated)
cv2.waitKey(0)

