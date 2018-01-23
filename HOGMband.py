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



from scipy import ndimage,signal
from pre import preprocess 

np.set_printoptions(threshold=np.nan)
f=np.array([])
#filter coefficients
#img=cv2.imread('/home/ubuntu/Documents/obj74__0.png',0)
def mband(img):
	h90=[0.022033327573,0.015381522616,-0.088169084245,0.051120949834,0.574161374258,0.717567366340,0.247558418377,-0.076963057605,-0.048477254777]
	h91=[0.048477254777,0.019991451948,-0.304530024033,0.165478923930,0.308884916012,-0.214155508410 ,-0.074865474330,0.028685132531,0.022033327573]
	h92=[0.031294135831,0.013248398005,-0.311552292833,0.497594326648,-0.235117092484,-0.020594576659,0.015375249485,0.009751852004,0]

	h0=np.asarray(h90)	#low pass
	h1=np.asarray(h91)	#band pass
	h2=np.asarray(h92)	#high pass


	img=preprocess(img)
	img=np.asarray(img)
	p=0
	row=(img.shape[0]/4)-1
	col=(img.shape[1]/4)-1
	f=[]
	for i in range(0,16):
		f.append(0)
	for r in range(0,img.shape[0]-row,row):
		for c in range(0,img.shape[1]-col,col):
	 		scale=img[r:r+row,c:c+col]

			[m,n]=scale.shape[:2]


			ft11 = [[0] * scale[1,:].ravel() for j in range(n)]
			ft11=np.asarray(ft11)

			ft12 = [[0] * scale[1,:].ravel() for j in range(n)]
			ft12=np.asarray(ft12)

			ft13 = [[0] * scale[1,:].ravel() for j in range(n)]
			ft13=np.asarray(ft13)

			for i in range(0,m):
				 ft11[i,:]=ndimage.convolve(scale[i,:].ravel(),h0,mode='wrap')
				 ft12[i,:]=ndimage.convolve(scale[i,:].ravel(),h1,mode='wrap')
				 ft13[i,:]=ndimage.convolve(scale[i,:].ravel(),h2,mode='wrap')
				 
			ftd1=signal.decimate(ft11.T,3)
			ftd2=signal.decimate(ft12.T,3)
			ftd3=signal.decimate(ft13.T,3)

			[m,n]=ftd1.shape[:2]

			ft1 = [[0] * ftd1[1,:] for j in range(m)]
			ft1=np.asarray(ft1)
			ft2 = [[0] * ftd1[1,:] for j in range(m)]
			ft2=np.asarray(ft2)
			ft3 = [[0] * ftd1[1,:] for j in range(m)]
			ft3=np.asarray(ft3)
			ft4 = [[0] * ftd1[1,:] for j in range(m)]
			ft4=np.asarray(ft4)
			ft5 = [[0] * ftd1[1,:] for j in range(m)]
			ft5=np.asarray(ft5)
			ft6 = [[0] * ftd1[1,:] for j in range(m)]
			ft6=np.asarray(ft6)
			ft7 = [[0] * ftd1[1,:] for j in range(m)]
			ft7=np.asarray(ft7)
			ft8 = [[0] * ftd1[1,:] for j in range(m)]
			ft8=np.asarray(ft8)
			ft9 = [[0] * ftd1[1,:] for j in range(m)]
			ft9=np.asarray(ft9)

			for i in range(0,m):
				ft1[i,:]=ndimage.convolve(ftd1[i,:],h0,mode='wrap')
				ft2[i,:]=ndimage.convolve(ftd1[i,:],h1,mode='wrap')
				ft3[i,:]=ndimage.convolve(ftd1[i,:],h2,mode='wrap')
	
				ft4[i,:]=ndimage.convolve(ftd2[i,:],h0,mode='wrap')
				ft5[i,:]=ndimage.convolve(ftd2[i,:],h1,mode='wrap')
				ft6[i,:]=ndimage.convolve(ftd2[i,:],h2,mode='wrap')
	
				ft7[i,:]=ndimage.convolve(ftd3[i,:],h0,mode='wrap')
				ft8[i,:]=ndimage.convolve(ftd3[i,:],h1,mode='wrap')
				ft9[i,:]=ndimage.convolve(ftd3[i,:],h2,mode='wrap')
	
			fm1=signal.decimate(ft1.T,3)
			fm2=signal.decimate(ft2.T,3)
			fm3=signal.decimate(ft3.T,3)
			fm4=signal.decimate(ft4.T,3)
			fm5=signal.decimate(ft5.T,3)
			fm6=signal.decimate(ft6.T,3)
			fm7=signal.decimate(ft7.T,3)
			fm8=signal.decimate(ft8.T,3)
			fm9=signal.decimate(ft9.T,3)

		#print fm2
		#print fm1
		#[m,n]=fm1.shape[:2]
		#print m,n
		#a = [[0] * fm1[1,:] for j in range(m)]
		#a=np.asarray(a)
			'''for j in range(90000):
				a.append(j)'''
			'''print fm1.shape
			fm1=np.append(fm1,fm1)
			fm1=np.append(fm1,fm2)
			fm1=np.append(fm1,fm3)
			fm1=np.append(fm1,fm4)
			fm1=np.append(fm1,fm5)
			fm1=np.append(fm1,fm6)
			fm1=np.append(fm1,fm7)
			fm1=np.append(fm1,fm8)
			fm1=np.append(fm1,fm9)
			print fm1
			print fm1.shape[:2]
			'''

			U1, s1, V3 = np.linalg.svd(fm1, full_matrices=True)
			U1, s2, V3= np.linalg.svd(fm2, full_matrices=True)
			U1, s3, V3= np.linalg.svd(fm3, full_matrices=True)
			U1, s4, V3= np.linalg.svd(fm4, full_matrices=True)
			U1, s5, V3= np.linalg.svd(fm5, full_matrices=True)
			U1, s6, V3= np.linalg.svd(fm6, full_matrices=True)
			U1, s7, V3= np.linalg.svd(fm7, full_matrices=True)
			U1, s8, V3= np.linalg.svd(fm8, full_matrices=True)
			U1, s9, V3= np.linalg.svd(fm9, full_matrices=True)

			s1=np.concatenate((s1,s2,s3,s4,s5,s6,s7,s8,s9))
			f[p]=s1
			#print s1
			print s1.shape
			p=p+1
			
	final=np.array([])
	final=np.append(final,f[0])
	final=np.append(final,f[1])
	final=np.append(final,f[2])
	final=np.append(final,f[3])
	final=np.append(final,f[4])
	final=np.append(final,f[5])
	final=np.append(final,f[6])
	final=np.append(final,f[7])
	final=np.append(final,f[8])
	final=np.append(final,f[9])
	final=np.append(final,f[10])
	final=np.append(final,f[11])
	final=np.append(final,f[12])
	final=np.append(final,f[13])
	final=np.append(final,f[14])
	final=np.append(final,f[15])
	print len(final)
	
	return final 




#**************************** Connectivity code **************
from pymongo import MongoClient
import pymongo
client=MongoClient('localhost',27017)
db1=client.fv
collection=db1.luffy
img=cv2.imread("/home/ubuntu/1.png",0)
#t0=time.time()
img_hist1=hog(img)
lbp=LocalBinaryPatterns(24,9)
img_hist1=lbp.describe(img)





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

