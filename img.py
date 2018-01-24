from pymongo import MongoClient
import gridfs
import os,cv2

#just to make sure we aren't crazy, check the filesize on disk:
#print os.path.getsize( r'/home/ubuntu/coil-20/obj1__0.png' )

#add the file to GridFS, per the pymongo documentation: http://api.mongodb.org/python/current/examples/gridfs.html
db = MongoClient().COIL20Images
fs = gridfs.GridFS( db )

i=0
g=289
while i<72:
	j=str(i)
	fileID = fs.put( open( r'/home/ubuntu/coil-20/obj5__'+j+'.png', 'r'), ID=str(g) )
	print g,i
	g=g+1
	i=i+1
	#out = fs.get(fileID).read()


