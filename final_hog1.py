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












#-------------------------- 1 ----------------------



#**************************** Connectivity code **************
from pymongo import MongoClient
import pymongo
client=MongoClient('localhost',27017)
db1=client.fv
collection=db1.luffy
img=cv2.imread("/home/ubuntu/1.png",0)
#t0=time.time()
img_hist1=hog(img)




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

quicksort(temp1,0,855)

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

'''	  
result = collection.find({'ID':73})
obj = next(result, None)
if obj:
  username= obj['descriptor']
  print len(obj['descriptor'] )
  print len(img_hist1.tolist())



#---------------------------- 2 ----------------------
img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__1.png",0)
#t0=time.time()
img_hist2=hog(img)
#print len(img_hist2)

img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__2.png",0)
#t0=time.time()
img_hist3=hog(img)
#print len(img_hist3)

img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__7.png",0)
#t0=time.time()
img_hist4=hog(img)
#print len(img_hist4)



img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__8.png",0)
#t0=time.time()
img_hist5=hog(img)
#print len(img_hist5)




img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__9.png",0)
#t0=time.time()
img_hist6=hog(img)
#print len(img_hist6)




img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj2__5.png",0)
#t0=time.time()
img_hist7=hog(img)
#print len(img_hist7)


img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj2__6.png",0)
#t0=time.time()
img_hist8=hog(img)
#print len(img_hist8)



img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj2__7.png",0)
#t0=time.time()
img_hist9=hog(img)
#print len(img_hist9)

'''

'''
i=0
temp1=0
temp2=0
temp3=0
temp4=0
temp5=0
temp6=0
temp7=0
temp8=0
temp9=0

#print img_hist1[14]-img_hist3[14]

#print img_hist1
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist1[i]
	if(cnt>=0):
		temp1=temp1+cnt
		#print "in if",temp1
	else:
		temp1=temp1+(-cnt)
		#print "in else",temp1
	i=i+1
print temp1



#i=0


'''
'''
#*************** 2******************
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist2[i]
	if(cnt>=0):
		temp2=temp2+cnt
		#print "in if",temp2
	else:
		temp2=temp2+(-cnt)
		#print "in else",temp2
	i=i+1
print temp2

i=0
#************** 3 ********************
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist3[i]
	if(cnt>=0):
		temp3=temp3+cnt
	else:
		temp3=temp3+(-cnt)
	i=i+1
print temp3

i=0
#********** 4 *********************
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist4[i]
	if(cnt>=0):
		temp4=temp4+cnt
	else:
		temp4=temp4+(-cnt)
	i=i+1
print temp4

#**************** 5 ******************
i=0
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist5[i]
	if(cnt>=0):
		temp5=temp5+cnt
	else:
		temp5=temp5+(-cnt)
	i=i+1
print temp5

#*************** 6   ******************
i=0
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist6[i]
	if(cnt>=0):
		temp6=temp6+cnt
	else:
		temp6=temp6+(-cnt)
	i=i+1
print temp6

#******************* 7 *******************
i=0
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist7[i]
	if(cnt>=0):
		temp7=temp7+cnt
	else:
		temp7=temp7+(-cnt)
	i=i+1
print temp7

#******************* 8  **********************
i=0
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist8[i]
	if(cnt>=0):
		temp8=temp8+cnt
	else:
		temp8=temp8+(-cnt)
	i=i+1
print temp8

#******************** 9  *******************
i=0
while(i<len(img_hist1)):
	cnt=img_hist1[i]-img_hist9[i]
	if(cnt>=0):
		temp9=temp9+cnt
	else:
		temp9=temp9+(-cnt)
	i=i+1
print temp9
'''

'''

dict1={temp1:1,temp2:2,temp3:3,temp4:4,temp5:5,temp6:6,temp7:7,temp8:8,temp9:9}

dict2={1:'obj1__0.png',2:'obj1__1.png',3:'obj1__3.png',4:'obj1__7.png',5:'obj1__8.png',6:'obj1__9.png',7:'obj2__5.png',8:'obj2__6.png',9:'obj2__7.png'}

sort=sorted(dict1)
print sort

i=0
j=1
print "THIS IS MANHATTAM DISTANCE WORKING:"
for i in sort:
	#print i
	print "image is ",dict2[dict1[i]]

'''

'''
#********************************** THIS REPRESENTS MANHATTAM DISTANCE WORKING ************************************************************

#-------------------------- 1 ----------------------

img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__0.png",0)
#t0=time.time()
img_hist1=hog(img)
#print img_hist1
#print len(img_hist1)
#---------------------------- 2 ----------------------
img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__1.png",0)
#t0=time.time()
img_hist2=hog(img)
#print len(img_hist2)

img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__2.png",0)
#t0=time.time()
img_hist3=hog(img)
#print len(img_hist3)

img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__7.png",0)
#t0=time.time()
img_hist4=hog(img)
#print len(img_hist4)



img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__8.png",0)
#t0=time.time()
img_hist5=hog(img)
#print len(img_hist5)




img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj1__9.png",0)
#t0=time.time()
img_hist6=hog(img)
#print len(img_hist6)




img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj2__5.png",0)
#t0=time.time()
img_hist7=hog(img)
#print len(img_hist7)


img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj2__6.png",0)
#t0=time.time()
img_hist8=hog(img)
#print len(img_hist8)



img=cv2.imread("/home/aniket/GLOBAL VECTOR/img/obj2__7.png",0)
#t0=time.time()
img_hist9=hog(img)
#print len(img_hist9)




i=0
temp1=0
temp2=0
temp3=0
temp4=0
temp5=0
temp6=0
temp7=0
temp8=0
temp9=0

#print img_hist1[14]-img_hist3[14]

#print img_hist1
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist1[i]),2)
	if(cnt>=0):
		temp1=temp1+cnt
		#print "in if",temp1
	else:
		temp1=temp1+(-cnt)
		#print "in else",temp1
	i=i+1
temp1=math.sqrt(temp1)
print temp1


i=0
#*************** 2******************
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist2[i]),2)
	if(cnt>=0):
		temp2=temp2+cnt
		#print "in if",temp2
	else:
		temp2=temp2+(-cnt)
		#print "in else",temp2
	i=i+1
temp2=math.sqrt(temp2)
print temp2

i=0
#************** 3 ********************
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist3[i]),2)
	if(cnt>=0):
		temp3=temp3+cnt
	else:
		temp3=temp3+(-cnt)
	i=i+1
temp3=math.sqrt(temp3)
print temp3

i=0
#********** 4 *********************
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist4[i]),2)
	if(cnt>=0):
		temp4=temp4+cnt
	else:
		temp4=temp4+(-cnt)
	i=i+1
temp4=math.sqrt(temp4)
print temp4

#**************** 5 ******************
i=0
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist5[i]),2)
	if(cnt>=0):
		temp5=temp5+cnt
	else:
		temp5=temp5+(-cnt)
	i=i+1
temp5=math.sqrt(temp5)
print temp5

#*************** 6   ******************
i=0
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist6[i]),2)
	if(cnt>=0):
		temp6=temp6+cnt
	else:
		temp6=temp6+(-cnt)
	i=i+1
temp6=math.sqrt(temp6)
print temp6

#******************* 7 *******************
i=0
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist7[i]),2)
	if(cnt>=0):
		temp7=temp7+cnt
	else:
		temp7=temp7+(-cnt)
	i=i+1
temp7=math.sqrt(temp7)
print temp7

#******************* 8  **********************
i=0
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist8[i]),2)
	if(cnt>=0):
		temp8=temp8+cnt
	else:
		temp8=temp8+(-cnt)
	i=i+1
temp8=math.sqrt(temp8)
print temp8

#******************** 9  *******************
i=0
while(i<len(img_hist1)):
	cnt=pow((img_hist1[i]-img_hist9[i]),2)
	if(cnt>=0):
		temp9=temp9+cnt
	else:
		temp9=temp9+(-cnt)
	i=i+1
temp9=math.sqrt(temp9)
print temp9



dict1={temp1:1,temp2:2,temp3:3,temp4:4,temp5:5,temp6:6,temp7:7,temp8:8,temp9:9}

dict2={1:'obj1__0.png',2:'obj1__1.png',3:'obj1__3.png',4:'obj1__7.png',5:'obj1__8.png',6:'obj1__9.png',7:'obj2__5.png',8:'obj2__6.png',9:'obj2__7.png'}

sort=sorted(dict1)
print sort

i=0
j=1
for i in sort:
	#print i
	print "image is ",dict2[dict1[i]]
	'''
