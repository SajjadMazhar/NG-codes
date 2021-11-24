#Simson 1/3rd rule
def integral_function(x):

	return 1+x**3+x*x

a=int(input("Enter lower limit= "))
b=int(input("\nEnter upper limit= "))
n=int(input("\nEnter number of sub intervals= "))
h=(b-a)/n
sum = integral_function(a) + integral_function(b)
m=4
for i in range(1,n):
	sum=sum+m*integral_function(a+i*h)
	m=6-m
sim=sum*(h/3)
print(f"The solution of the given integeral problem is {sim}")


