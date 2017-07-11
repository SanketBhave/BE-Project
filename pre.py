import cv2,math
import numpy as np

img=cv2.imread("/home/ubuntu/Downloads/coil-100/obj74__0.png",0)

ret,thresh =cv2.threshold(img,80,255,cv2.THRESH_BINARY)
#thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\cv2.THRESH_BINARY,11,2)
#thresh=cv2.erode(thresh,None,iterations=2)
#thresh=cv2.dilate(thresh,None,iterations=2)
ret1,thresh1=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
im,contours,hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=max(contours,key=cv2.contourArea)
extLeft=tuple(cnt[cnt[:,:,0].argmin()][0])
extRight=tuple(cnt[cnt[:,:,0].argmax()][0])
extTop = tuple(cnt[cnt[:, :, 1].argmin()][0])
extBot = tuple(cnt[cnt[:, :, 1].argmax()][0])
val =(float) (extBot[0]-extTop[0])/(extBot[1]-extTop[1]) # calculate slope between the two points
val1 =(float) (extRight[0]-extLeft[0])/(extRight[1]-extLeft[1]) # calculate slope between the two points
if val1>val:
	val=val1

rot_angle=math.degrees(math.atan(val))


cols,rows=thresh.shape
M=cv2.getRotationMatrix2D((rows/2,cols/2),90-rot_angle,1)
dst=cv2.warpAffine(thresh,M,(rows,cols))

cv2.imshow('Image3',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ellipse=cv2.fitEllipse(cnt)
#angle=ellipse[2]
#M1=cv2.getRotationMatrix2D((cols/2,rows/2),90-angle,1)
#dst1=cv2.warpAffine(thresh,M1,(cols,rows))

#cv2.imshow('Image4',dst1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

x,y,w,h=cv2.boundingRect(cnt)
crop_img=dst[y:y+h,x:x+w]
resized_image=cv2.resize(crop_img,(128,128))
cv2.imshow('Image6',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
