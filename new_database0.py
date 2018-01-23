import cv2
import numpy as np
from numpy import linalg as la
import time,gridfs
import math
from QuickSort import quicksort
from pymongo import MongoClient
import pymongo
client=MongoClient('localhost',27017)
db1=client.HOGCOIL20
collection=db1.features

np.set_printoptions(threshold='nan')
def hog(img,g):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bin_n = 16 # Number of bins
    bin = np.int32(bin_n*ang/(2*np.pi))
   # print bin

    bin_cells = []
    mag_cells = []
    cellx = celly = 8
    for i in range(0,img.shape[0]/celly):
	for j in range(0,img.shape[1]/cellx):
	    bin_cells.append(bin[i*celly : i*celly+celly, j*cellx : j*cellx+cellx])
	    mag_cells.append(mag[i*celly : i*celly+celly, j*cellx : j*cellx+cellx])   
	    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
	    hist = np.hstack(hists)
	    
    # transform to Hellinger kernel
    eps = 1e-7
    hist /= hist.sum() + eps
    hist = np.sqrt(hist)
    hist /= la.norm(hist) + eps
    
    #hist	
    collection.insert({"ID":g,"descriptor":hist.tolist()}) 
    return hist


	    
	    
	    
	    
i=0
g=217

while(i<72):
	j=str(i)
	#k=g+1
	img=cv2.imread("/home/ubuntu/coil-20/obj4__"+j+".png",0)
	
	#var="/home/ubuntu/coil-20/obj3__"+j+".png"
	#print var
	hog(img,g)

	
	print g,i
	i=i+1
	g=g+1	
