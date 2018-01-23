import cv2
import numpy as np
from numpy import linalg as la
import time,gridfs
import math
from QuickSort import quicksort

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



#**************************** Connectivity code **************
from pymongo import MongoClient
import pymongo
client=MongoClient('localhost',27017)
db1=client.hoglbp
collection=db1.features
img=cv2.imread("/home/ubuntu/1.png",0)
#t0=time.time()
img_hist1=hog(img)
lbp=LocalBinaryPatterns(24,9)
img_hist=lbp.describe(img)

img_hist1=np.append(img_hist1,img_hist)
print len(img_hist1)


#print img_hist1

dict1={}
temp1=[]
for i in range(0,856):
	temp1.append(0)

j=1
m=0
result = collection.find()
obj = next(result, None)
while(obj!=None):
	  i=0
	  username= obj['descriptor']
	  print len(username),obj['ID']
	  while(i<len(img_hist1)):
		cnt=img_hist1[i]-username[i]
		if(cnt>=0):
			temp1[m]=temp1[m]+cnt
			#print "in if",temp1
		else:
			temp1[m]=temp1[m]+(-cnt)
			#print "in else",temp1
		i=i+1
	 # print temp1+"___"+j
	  tt=str(temp1[m])
	  #k=str(j)
	  print tt+"---"+str(obj['ID'])
	  #temp1=0
	  dict1[temp1[m]]=obj['ID']
	  j=j+1
	  m=m+1
	  obj = next(result, None)
print temp1
quicksort(temp1,0,50)


m=0
id1=[]
while m<856:
	id1.append(dict1[temp1[m]])
	m=m+1
print id1	
db=client.imagedb
coll=db.fs.files
i=0
fs=gridfs.GridFSBucket(db)
while i<25:
	j=str(i)
	file=open("r"+j+".png",'wb+')
	result=coll.find_one({"ID":str(id1[i])})
	fs.download_to_stream(result['_id'],file)
	file.seek(0)
	i=i+1

