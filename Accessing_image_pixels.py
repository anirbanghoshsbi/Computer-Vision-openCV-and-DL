# import the libraries
import opoencv2
import argparse

ap = ArgumentParser()
ap.add_argument("-i","--image",help = "path to the image", required = True)
args = vars(ap.parse_args())

# load image from the disk
image = cv2.imread(args["image"])
# display the pixel at location [1,1]
(b ,g, r) = image[1,1] # this is because the openCV stores (b,g,r) instead of (r,g,b)
print("The image pixels at [1,1] is {r} , {g} ,{b}" .format(r,g,b))
# divide the image into four parts
#calculate the centre
(h , w) = image[:2]
(cY , cX) = (h//2 , w//2)
# display the top  left
image_left = image[0:cY , 0:cX]
#display the top right
image_right = image[0:cY ,cX:w]
#display bottom left
image_bleft=image[cY:h,0:cX]
#display bottom right
image_bright = image[cY:h , cX:w]

# show these images
cv2.imshow("The top left {} image , top right image {} , bottom left image {} , bottom right image {}" . format(image_left , image_right , image_bleft , image_bright))

# Change the color of the top left image slice to green
image[0:cX , 0:cY] = (0,255,0) # just as I would work with numpy (r,g,b)
# show image
cv2.imshow("The image is {}" .format(image))
cv2.waitKey(0)
