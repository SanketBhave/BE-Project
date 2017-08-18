import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
img1 = cv2.imread('1.png',0)
laplacian = cv2.Laplacian(img1,cv2.CV_8U)


print img1

#sobelx = cv2.Sobel(sobely,cv2.CV_64F,1,0,ksize=5)


def MakeSaltAndPepperNoise (Image, SaltNum, PepperNum):
 CopyImage = Image.copy()
 nChannel = 0

 # Get Image size
 Width = CopyImage.shape[0]
 Height = CopyImage.shape[1]
 
 # If image is grayscale, it not have Image.shape[2]
 # so it raise IndexError exception
 try:
  nChannel = CopyImage.shape[2]
 except IndexError:
  nChannel = 1

 # Make Salt Noise
 for Salt in range(0, SaltNum):
  # Generate Random Position
  RWidth = random.randrange(0, Width)
  RHeight = random.randrange(0, Height)
  # Make Noise
  if nChannel > 1:
   for c in range(0, nChannel):
    CopyImage[RWidth, RHeight, c] = 255
  else:
   CopyImage[RWidth, RHeight] = 255

 # Make Pepper Noise
 for Pepper in range(0, PepperNum):
  # Generate Random Position
  RWidth = random.randrange(0, Width)
  RHeight = random.randrange(0, Height)
  # Make Noise
  if nChannel > 1:
   for c in range(0, nChannel):
    CopyImage[RWidth, RHeight, c] = 0
  else:
   CopyImage[RWidth, RHeight] = 0

 return CopyImage

img1=MakeSaltAndPepperNoise (img1, 300, 300)
img=cv2.medianBlur(img1,3)
edges = cv2.Canny(img,50,200)
sobely = cv2.Sobel(edges,cv2.CV_8U,1,0,ksize=5)



print sobely

plt.subplot(2,2,2),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


plt.subplot(2,2,3),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])


plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
