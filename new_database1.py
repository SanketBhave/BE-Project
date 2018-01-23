import cv2,math
from skimage import feature
from scipy import ndimage,signal
from pre import preprocess 
import numpy as np
from numpy import linalg as la
from pymongo import MongoClient
from itertools import izip
#import numpy as np
#import cv2
import skimage
from skimage import filter


client=MongoClient('localhost',27017)
db=client.lbp
collection=db.features

np.set_printoptions(threshold='nan')
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
		collection.insert({"ID":g,"descriptor":hist.tolist()}) 

	
	
	
    
    #hist	
    
    #print len(hist)
    
	    
	    
	    
	    
	    
	    
i=431
g=856

while(i<432):
	j=str(i)
	#k=g+1
	img=cv2.imread("/home/ubuntu/Downloads/UCIDPNG/"+j+".png",0)
	
	#var="/home/ubuntu/coil-20/obj3__"+j+".png"
	#print var
	lbp=LocalBinaryPatterns(24,9)
	lbp.describe(img)

	
	print g,i
	i=i+1
	g=g+1	
