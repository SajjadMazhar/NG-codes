print("hello")
lis=[1,8,6]
g=lis[0]
i=1
while True:
	if g<lis[i]:
		temp=g
		g=lis[i]
		lis[i]=temp
	elif i>len(lis):
		break
		
print(g)
	
	