import cv2
import numpy as np
from PIL import ImageTk, Image
from matplotlib import pyplot as plt

#Reading the image as grayscale, normalizing it and showing it
img = cv2.imread('pop.png',0)
img=img/255.0
cv2.imshow('original',img)

#Singular Value Decomposition (SVD) and finding maximum singular value
U, s, V = np.linalg.svd(img, full_matrices=True)
nrows=len(U)
ncols=len(V)
dg=len(s)
S = np.zeros((nrows, ncols))
S[:dg, :dg] = np.diag(s)
Max1=np.max(S)

#Generarting the random number matrix and doing SVD
A = np.random.normal(loc =0.5, scale =1, size=(nrows, ncols))
U1, s1, V1 = np.linalg.svd(A, full_matrices=True)
S1 = np.zeros((nrows, ncols))
S1[:dg, :dg] = np.diag(s1)
Max2=np.max(S1)

#Calculating zeta
zeta=Max2/Max1

#Modifying the original S matrx
Snew=zeta*S

#Reconstructing the image
newimg=np.dot(U, np.dot(Snew,V))
newimg=np.uint8(newimg*255.0)

#Showing the new image
cv2.imshow('newimg',newimg)

#Showing the histograms for original and modified images
plt.figure()
plt.hist(img.ravel(),256,[0,256])
plt.figure()
plt.hist(newimg.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()