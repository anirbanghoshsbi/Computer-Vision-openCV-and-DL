# import dependencies
import cv2
import numpy as np

# initialize a canvas

canvas = np.zeros((300,300,3) , dtype='uint8')

#draw a green line from top left corner of the canvas to the bottom right corner

green = (0 , 0 ,255)
red=(0,255,0)
color1=(105,155,135)
color2= (175 , 15, 189)
#draw a line from (0,0) , (300 , 300)

cv2.line(canvas , (0,0) , (300 , 300) , green)
cv2.imshow("Canvas" , canvas)


#Draw a red line 3 pixel thick

#cv2.line(canvas , (200 ,0) , (300,0) , red  , 3)
#cv2.imshow("Canvas" , canvas)


# Draw another line that is 5 pixel long and this time vertical

cv2.line(canvas , (200,0) ,(0,200) ,color1 , 5)
cv2.imshow("Canvas" , canvas) 
cv2.waitKey(0)

cv2.line(canvas , (200,0) , (200 , 300) , color2 , 15)
cv2.imshow("canvas" , canvas)
cv2.waitKey(0)

#Draw a rectangle 
cv2.rectangle( canvas , (10,10) , (50,50) , green , 3)
cv2.imshow("canvas" , canvas)
cv2.waitKey(0)

# Draw a Circle 
# first let me get the centre of the canvas
canvas=np.zeros((300 , 300 , 3) , dtype ='uint8')
(centerX , centerY)= (canvas.shape[1]//2 , canvas.shape[0]//2)
white =(255,255,255)

for r in range(0 , 150 , 25):
	cv2.circle(canvas , (centerX , centerY) , r , white)
cv2.imshow("canvas" , canvas)
cv2.waitKey(0)

# lets go crazy and draw random circles
for i in range(0 , 50):
	radius=np.random.randint(5 , high=150)
	color =np.random.randint(0, high = 256 , size =(3,)).tolist()
	pt=np.random.randint(0 , high= 300 , size= (2,))
	cv2.circle(canvas , tuple(pt) , radius ,color ,-1)
cv2.imshow("Canvas" , canvas)
cv2.waitKey(0)	
