#Importing openCV and numpy
import cv2
import numpy as np

#Function, "nothing" which does nothing
def nothing(x):
    pass

#Reading the image in "img"
img = cv2.imread('hsn.jpg')

#Resizing the image to double the size using resize function and cubic interpolation
resized_cubic = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#Saving the doubled image to a file
cv2.imwrite('hsn_dbl.jpg', resized_cubic)

#Copying the original image to a variable, img_gam to be used for gamma correction
img_gam=img

#Create a window named image
cv2.namedWindow('image')

#Create a trackbar named "R" inside that window with range from 1 to 30 and calling "nothing" function
cv2.createTrackbar('R','image',1,30,nothing)

#Looping forever unless an Esc key is pressed
while(1):
    k = cv2.waitKey(1) & 0xFF   #the code for a key pressed
    if k == 27:                 #if it's Esc
        break                   #get out of the loop

    #Get the value from the trackbar into r
    r = cv2.getTrackbarPos('R','image')   
    r=r/10.0 #divide it by 10 to enable using fractions < 1

    #The gamma correction; normalize the image, raise every pixel value to a power, then get values back to 0-255 range
    img_gam=img/255.0
    img_gam=cv2.pow(img_gam,r)
    img_gam=np.uint8(img_gam*255)

    #Combining the 2 images and then show it
    both=np.hstack((img,img_gam))
    cv2.imshow('image',both)
    print(r) #just showing the current value of gamma

cv2.destroyAllWindows() #close the window