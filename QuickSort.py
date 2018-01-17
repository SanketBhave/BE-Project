import threading
import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('number.xml').getroot()
print e.findall('data')
'''
def partition(arr,left,right):
	i=left
	j=right
	pivot=arr[(left+right)/2]
	while(i<=j):
		while(arr[i]<pivot):
			i=i+1
		while(arr[j]>pivot):
			j=j-1
		if(i<=j):
			tmp=arr[i]
			arr[i]=arr[j]
			arr[j]=tmp
			i=i+1
			j=j-1
	return i



def quicksort( arr, left,right):
	print threading.current_thread()
	index=partition(arr,left,right)
	athread=None
	bthread=None
	if(left<index-1):
		athread=threading.Thread(target=lambda:quicksort(arr,left,index-1))
		athread.start()
	if(index<right):
		bthread=threading.Thread(target=lambda:quicksort(arr,index,right))
		bthread.start()
	if athread is not None:athread.join()
	if bthread is not None:bthread.join()	

arr=[]
n=input("Enter number of elements of array")
i=0
while(i<n):
	arr.append(input("Enter the element"))
	i=i+1
left=0
right=n-1
quicksort(arr,left,right)

print arr
'''
