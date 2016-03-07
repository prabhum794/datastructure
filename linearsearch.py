def linearsearch(l):
	found = False
	num = int(raw_input())
	for i in range(len(l)):
		if l[i] == num:
			found = True
			pos = i+1
			break
	if found == True:
		print "Element found at position : ",pos
	else:
		print "Element not found."

alist = [25,88,1402,133,15,99,108,15,22]
linearsearch(alist)
