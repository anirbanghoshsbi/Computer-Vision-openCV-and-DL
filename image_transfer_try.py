''' In the given code we try to transfer the color in the source image 
to that in the target image. This is the implementation based on pyimagesearch.com
The algorithm goes like this:

    Step 1: Input a source and a target image. The source image contains the color space that you want your target image to mimic. In the figure at the top of  this page, the sunset image on the left is my source, the middle image is my target, and the image on the right is the color space of the source applied to the target.
    Step 2: Convert both the source and the target image to the L*a*b* color space. The L*a*b* color space models perceptual uniformity, where a small change in an amount of color value should also produce a relatively equal change in color importance. The L*a*b* color space does a substantially better job mimicking how humans interpret color than the standard RGB color space, and as you’ll see, works very well for color transfer.
    Step 3: Split the channels for both the source and target.
    Step 4: Compute the mean and standard deviation of each of the L*a*b* channels for the source and target images.
    Step 5: Subtract the mean of the L*a*b* channels of the target image from target channels.
    Step 6: Scale the target channels by the ratio of the standard deviation of the target divided by the standard deviation of the source, multiplied by the target channels.
    Step 7: Add in the means of the L*a*b* channels for the source.
    Step 8: Clip any values that fall outside the range [0, 255]. (Note: This step is not part of the original paper. I have added it due to how OpenCV handles color space conversions. If you were to implement this algorithm in a different language/library, you would either have to perform the color space conversion yourself, or understand how the library doing the conversion is working).
    Step 9: Merge the channels back together.
    Step 10: Convert back to the RGB color space from the L*a*b* space.

'''
#usage python image_transfer_try.py -s <path to source image> -t <path to targetimage> -t <path to the place where image will be saved>

#import the necessary package
import cv2
import argparse
import numpy as np

def show_image(title,image , width= 300):
	r=width/float(image.shape[1])
	dim = (width , int(image.shape[0]*r))
	resized=cv2.resize(image , dim ,interpolation=cv2.INTER_AREA)
	cv2.imshow(title , resized)
	

def color_transfer(source , target):
	source=cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
	target=cv2.cvtColor(target , cv2.COLOR_BGR2LAB).astype("float32")
	
	(lMeanScr, lStdScr , aMeanScr ,aStdScr, bMeanScr , bStdScr) =image_stats(source)
	(lMeanTar, lStdTar , aMeanTar ,aStdTar, bMeanTar , bStdTar) =image_stats(target)

	#substract the mean from  the target image
	(l,a,b)=cv2.split(target)
	l-=lMeanTar
	a-=aMeanTar
	b-=bMeanTar

	#scale the image by the standard deviation
	l=(lStdTar/lStdScr)*l
	a=(aStdTar/lStdScr)*a
	b=(bStdTar/lStdScr)*b

	# add in the source mean
	l+=lMeanScr
	a+=aMeanScr
	b+=bMeanScr

	#clip the intensities with in [0,255]
	l=np.clip(l,0,255)
	a=np.clip(a,0,255)
	b=np.clip(b,0,255)
	
	#transfer the image by merging the l,a,b channels and then transfering it to color forrmat
	transfer=cv2.merge([l,a,b])
	transfer=cv2.cvtColor(transfer.astype('uint8'),cv2.COLOR_LAB2BGR)
	return transfer

def image_stats(image):
	#get the stats for the images like the means , Std etc.
	(l,a,b)=cv2.split(image)
	(lMean  , lStd) =(l.mean() ,l.std())
	(aMean , aStd)=(a.mean() , a.std())
	(bMean ,bStd)=(b.mean() ,b.std())
	return (lMean , lStd , aMean , aStd , bMean , bStd)

# construct the argument parser
ap=argparse.ArgumentParser()
ap.add_argument("-s","--source", required=  True , help = 'The path to the Source')
ap.add_argument("-t" , "--target", required =True , help ='The path to the target')
ap.add_argument("-o" , "--output" , required = True  , help ='The path to the saved file')

args=vars(ap.parse_args())

# load the image 
source = cv2.imread(args['source'])
target = cv2.imread(args['target'])

#transfer color of the source to the target 
transfer=color_transfer(source , target)

# check if the output image needs to be saved

if args["output"] is not None:
	cv2.imwrite(args["output"] , transfer)

#show the images and wait for the key press
show_image("Original", source)
show_image("Target" , target)
show_image("Transfer" , transfer)
cv2.waitKey(0)

	 
	
