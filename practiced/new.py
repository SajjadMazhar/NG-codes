def fibonac(reaching_value):
	f1=1
	f2=1
	print("f1= ",f1)
	print("f2= ",f2)
	counter=2
	while True:
		if f2<reaching_value:
			f3=f1+f2 
			counter+=1
			print(f"f{counter} = {f3}")
			f1=f2
			f2=f3
		else:
			print(f"The f{counter} is the first term to reach {reaching_value}")
			break	

		
value=int(input("Enter the reaching value: "))	
fibonac(value)

