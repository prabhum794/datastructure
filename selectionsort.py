alist = [25,88,1402,133,15,99,108,13,22]

def selectionsort(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[j]<l[i]:
				l[i],l[j] = l[j],l[i]
	print l


selectionsort(alist)