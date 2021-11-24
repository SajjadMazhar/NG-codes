def decimal(bin):
	sbin=str(bin)
	blen=len(sbin)
	sum=0
	for i in range(0,blen):
		n=bin%10
		bin=bin//10
		sum=sum+n*(2**i)
	print("The decimal of the given binary is:",sum)
	
def binary(dec):
	rem=dec%2
	bin=str(rem)
	dec=dec//2
	while(dec>0):
		rem=dec%2
		bin=str(rem)+bin
		dec=dec//2
	print("Binary of the given decimal is:",bin)
	
if __name__=='__main__':
	dec=int(input("enter a decimal value: "))
	binary(dec)	

	bin=int(input("Enter a binary: "))
	decimal(bin)
