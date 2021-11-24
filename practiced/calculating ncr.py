def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact
		
x=int(input("enter n"))
y=int(input("enter r"))
n1=factorial(x)
n2=factorial(y)
n3=factorial(x-y)
ncr=n1/(n2*n3)
print("The ",x,"C",y,"= ",ncr)