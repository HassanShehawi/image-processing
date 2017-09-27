#Importing the openCV library
import cv2

#Saving the image in a variable called img
img = cv2.imread('hyp.png')

#Writing the image to a file named hyp1 with png extension
cv2.imwrite('hyp1.png', img)

#Showing the image in a window with a title "Original"
cv2.imshow('original',img)

#Wait till the Esc button on keyboard is pressed
cv2.waitKey(0)

#Close the window
cv2.destroyAllWindows()
