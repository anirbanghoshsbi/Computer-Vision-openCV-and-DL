# USAGE
# python compare.py
'''
based on pyimagesearch.com
the 'Mean Squared Error' between the two images is the
sum of the squared difference between the two images;
NOTE: the two images must have the same dimension


MSE is dead simple to implement — but when using it for similarity, we can run into problems. The main one being that large distances between pixel intensities do not necessarily mean the contents of the images are dramatically different. I’ll provide some proof for that statement later in this post, but in the meantime, take my word for it.

It’s important to note that a value of 0 for MSE indicates perfect similarity. A value greater than one implies less similarity and will continue to grow as the average difference between pixel intensities increases as well

The SSIM method is clearly more involved than the MSE method, but the gist is that SSIM attempts to model the perceived change in the structural information of the image, whereas MSE is actually estimating the perceived errors. There is a subtle difference between the two, but the results are dramatic.

Furthermore, the equation is used to compare two windows (i.e. small sub-samples) rather than the entire image as in MSE. Doing this leads to a more robust approach that is able to account for changes in the structure of the image, rather than just the perceived change.

The parameters to Equation 2 include the (x, y) location of the N x N window in each image, the mean of the pixel intensities in the x and y direction, the variance of intensities in the x and y direction, along with the covariance.

Unlike MSE, the SSIM value can vary between -1 and 1, where 1 indicates perfect similarity.
'''
# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import argparse
import imutils

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
        print("mse" , m)
	print("ssim",s)
	return None

# load the images -- the original, the original + contrast,
# and the original + photoshop
# load the images -- the original, the original + contrast,
# and the original + photoshop
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True,
    help="First image to compare")
ap.add_argument("-i2", "--image2", required=True,
    help="Second image to compare")
'''ap.add_argument("-i3", "--image3", required=True,
    help="Second image to compare")'''
args = vars(ap.parse_args())

def normalize(image, lenX, lenY):
    resized1 = cv2.resize(image, (lenX, lenY))
    resized2 = imutils.resize(resized1, width=100)
    
    '''blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    (_, thresh) = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY_INV)'''
    return resized2



# convert the images to grayscale
image1 = cv2.imread(args["image1"])
image2 = cv2.imread(args["image2"])
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#resize the images
maxX = max(image1.shape[1], image2.shape[1])
maxY = max(image1.shape[0], image2.shape[0])

normImage1 = normalize(image1, maxX, maxY)
normImage2 = normalize(image2, maxX, maxY)


cv2.imshow("normImage1", normImage1)
cv2.imshow("normImage2", normImage2)
cv2.waitKey(0)
print('The similiarity between Image 1 and Image1')
compare_images(normImage1, normImage1)
print('The similiarity between Image 1 and Image2')
compare_images(normImage1,normImage2)
print('The similiarity between Image2 and Image2')
compare_images(normImage2,normImage2)
cv2.waitKey(0)


