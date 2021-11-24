print("Enter last term max value in the series")
n=int(input())
a=1
b=1
print("the fibbonacci series is given as")
print(a,b,end=" ")
i=1
while(i>0):	
	c=a+b
	if c<=n:
		print(c,end=" ")
		a=b
		b=c 
	else:
		break