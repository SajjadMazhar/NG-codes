import bin_to_dec
import dec_to_bin_compact
while(1):
	op=input("Enter 'b' to get binary as output or 'd' to get decimal as output:")
	if op=='b':
		value=int(input("Enter a decimal value:"))
		result=dec_to_bin_compact.binary(value)
	elif op=='d':
		value=int(input("Enter a binary value:"))
		result=bin_to_dec.decimal(value)
	else:
		print("Invalid input!!")
	ex=int(input("Enter 1 to calculate again or any other number to exit:"))
	if ex==1:
		continue
	else:
		print("Successfully exited the program...")
		break
	
