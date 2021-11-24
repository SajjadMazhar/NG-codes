def fun1(r,b):
	if c==True:
		for i in range(1,r+1):
			print(i*"*")
	elif c==False:
		for i in range(0,r):
			print((r-i)*"*")
		
r=int(input("enter the rows"))
b=int(input("enter 0 or 1"))
c=bool(b)
fun1(r,b)	