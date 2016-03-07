def sort(l):
	for i in range(len(l)):
		for j in range(len(l)-1):
			if l[j]>l[j+1]:
				l[j],l[j+1] = l[j+1],l[j]
	print l
def insertnumber():
	print "Input numbers"
	l = [int(x) for x in raw_input().split()]
	sort(l)

insertnumber()