def add_sub(n1,n2):
	sum = n1 + n2
	sub = n1 - n2
	div = n1 / n2
	mul = n1 * n2
	rem = n1 % n2
	return sum, sub,div,mul,rem
index = 0
while(index<1):
	m=int(input("Enter the first number= "))
	t=int(input("Enter the second number= " ))
	op=input("Enter a mathematical operator or enter R/r to find the remainder\n")
	operated = add_sub(m,t)
	if op=='+':
		print(m," + ",t, " = ", operated[0])
	elif op=='-':
		print(m," - ",t, " = ", operated[1])
	elif op=='/':
		print(m," / ",t, " = ", operated[2])
	elif op=='*':
		print(m," x ",t, " = ", operated[3])
	elif op=='r' or op=='R':
		print("mod(",m ,",",t,") = ", operated[4])
	else:
		print("Please, enter a valid input operator.")