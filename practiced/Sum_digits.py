number=int(input("Enter a positive interger: "))
sum=0
while number!=0:	
	remainder=number%10
	sum=sum+remainder
	number=number//10
	
print("Sum of digits of the given number: ",sum)