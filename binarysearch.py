def binarysearch(l,num):
	found = False
	low = 0
	high = len(l)
	while found is not True:
		if high<=low:
			break
		mid = low+(high-low)/2
		print l[low:high]
		print mid
		if num == l[mid]:
			found = True
		elif num > l[mid]:
			low = mid +1
		elif num < l[mid]:
			high = mid -1 
	if found:
		print "Found"
	else:
		print "Not Found"

	

alist = [25,88,1402,133,15,99,108,13,22]
alist =  sorted(alist)
num = 23
binarysearch(alist,num)