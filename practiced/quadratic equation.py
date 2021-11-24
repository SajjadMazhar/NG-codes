print("****************************************************************")
print("***************Quadratic Equation Root Calculator***************")
print("****************************************************************")
import math
while(1):
	a=int(input("Enter the coefficient of x² as a ="))
	b=int(input("Enter the coefficient of x as b ="))
	c=int(input("Enter the constant c ="))
	print("\n")
	d = b*b-4*a*c
	if d > 0:
		root1=(-b + math.sqrt(d))/(2*a)
		root2=(-b - math.sqrt(d))/(2*a)
		print(f"The roots are real and unequal, the roots are, \n{root1},{root2}")
		in_ex=int(input("\nEnter 1 to calculate again or 0 to exit..!\n"))
		if in_ex==1:
			continue
		elif in_ex==0:
			 print("successfully exited the system")
			 break			 
			 
	elif d < 0:
		real_root_1 = -b/(2*a)
		real_root_2 = real_root_1
		i_root_1 = math.sqrt(-d)/(2*a)
		i_root_2 = -i_root_1
		print(f"The roots are imaginary, and the real part of roots are,\n {real_root_1},{real_root_2} \nand the imaginary part of roots are, \n{i_root_1},{i_root_2}")
		in_ex=int(input("\nEnter 1 to calculate again or 0 to exit..!\n"))
		if in_ex==1:
			continue
		elif in_ex==0:
			 print("successfully exited the system...!!")
			 break	
	else:
		root1 = -b/(2*a)
		root2 = root1
		print(f"The roots are real and equal, the roots are,\n {root1},{root2}")
		in_ex=int(input("\nEnter 1 to calculate again or 0 to exit..!\n"))
		if in_ex==1:
			continue
		elif in_ex==0:
			 print("successfully exited the system")
			 break 	