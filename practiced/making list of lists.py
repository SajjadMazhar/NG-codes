

list=[1,2,3,4,5,6,7,8,9]
ilist=[]
flist=[]
count=0
while(1):
	if count<3:
		for i in range(3):
			ilist.append(list[i])
		count=3
		flist.append(ilist)
		ilist=[]
	elif count<6:
		for i in range(3,6):
			ilist.append(list[i])
		count=6
		flist.append(ilist)
		ilist=[]
	elif count<9:
		for i in range(6,9):
			ilist.append(list[i])
		count=9
		flist.append(ilist)
	else:
		print(flist)
		break

	