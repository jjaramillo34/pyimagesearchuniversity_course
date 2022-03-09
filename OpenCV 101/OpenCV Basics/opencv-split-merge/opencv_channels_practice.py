# USAGE
# python opencv_channels_practice.py

# import the necessary packages
import argparse
import cv2
import numpy as np

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
    help="path to the input image")
args = vars(ap.parse_args())

# load the input image and grab each channel -- note how OpenCV represents images 
# as NumPy arrays with channels in Blue, Green, Red ordeding rather Red, Green, 
# Red ordeding rather than Red, Green, Blue
# load the image and display it to our screen
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)
cv2.imshow("Original", image)


# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merge the iamge back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
