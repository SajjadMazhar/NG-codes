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