# USAGE
# python morphological_ops_practice.py --image pyimagesearch_logo.png

# import the necessary packages
import argparse
import cv2

#construct the argument parser and the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the input image")
args = vars(ap.parse_args())

# load image, convert to grayscale, and display it to out screen
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# apply a series of erosions
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)
    
# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# apply a series of dilations
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)
    
# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (4, 4), (5, 5)]

# loop over the kernels sizes
for kernelSize in kernelSizes:
    # construct a rectagular kernel from the current size then apply an 
    # "opening" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening : ({} {})".format(
        kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernels sizes again
for kernelSize in kernelSizes:
    # construct a rectagular kernel from the current size then apply an 
    # "closing" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing : ({} {})".format(
        kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernels a final time
for kernelSize in kernelSizes:
    # construct a rectagular kernel from the current size then apply an 
    # "gradient" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Closing : ({} {})".format(
        kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)


