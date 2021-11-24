print("enter first number")
x=int(input())
z=(input("enter the mathematical operator(eg. +,-,* or /)\n"))
print("enter second number")
y=int(input())
if z == "+":
	if x==56 : 
		if y==9 :
			print("answer is\t77")
		else:
			print("answer is\t",x+y)
	else:
			print("answer is\t",x+y)
elif z == "-" :
	print("answer is\t",x-y)
elif z == "*" :
	if x==45:
		if y==3:
			print("answer is\t555")
		else:
			print("answer is\t",x*y)
	else:
		print("answer is\t",x*y)
elif z == "/" :
	if x==56:
		if y==6:
			print("answer is\t4")
		else:
			print("answer is\t",x/y)
	else:
		
		print("answer is\t",x/y)
else:
	print("the operator entered is invalid")