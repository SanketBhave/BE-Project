import cv2
import numpy as np
from numpy import linalg as la
import time,gridfs
import math,pymongo
from QuickSort import quicksort
from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.hoglbp
collection=db.features

np.set_printoptions(threshold='nan')
def hog(img):
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
    #collection.insert({"ID":3,"descriptor":hist.tolist()}) 
    return hist



from skimage import feature
class LocalBinaryPatterns:
	def __init__(self, numPoints, radius):
		# store the number of points and radius
		self.numPoints = numPoints
		self.radius = radius
 
	def describe(self, image, eps=1e-7):
		# compute the Local Binary Pattern representation
		# of the image, and then use the LBP representation
		# to build the histogram of patterns
		lbp = feature.local_binary_pattern(image, self.numPoints,
			self.radius, method="uniform")
		(hist, _) = np.histogram(lbp.ravel(),
			bins=np.arange(0, self.numPoints + 3),
			range=(0, self.numPoints + 2))
 
		# normalize the histogram
		hist = hist.astype("float")
		hist /= (hist.sum() + eps)
 
		# return the histogram of Local Binary Patterns
		return hist


i=4
g=364

while(i<365):
	j=str(i)
	#k=g+1
	img=cv2.imread("/home/ubuntu/Downloads/UCIDPNG/"+j+".png",0)
	
	#var="/home/ubuntu/coil-20/obj3__"+j+".png"
	#print var
	hist1=hog(img)
	lbp=LocalBinaryPatterns(24,9)
	hist2=lbp.describe(img)
	hist1=np.append(hist1,hist2)
	print len(hist1)
	collection.insert({"ID":g,"descriptor":hist1.tolist()})
	
	print g,i
	i=i+1
	g=g+1	
