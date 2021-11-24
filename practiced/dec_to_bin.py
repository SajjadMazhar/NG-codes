def binary(dec):
	rem=dec%2
	bin=str(rem)
	dec=dec//2
	while(dec>0):
		rem=dec%2
		bin=str(rem)+bin
		dec=dec//2
	print("Binary of the given decimal is:",bin)
	
decimal=int(input("Input a Decimal value: "))
binary(decimal)
	
