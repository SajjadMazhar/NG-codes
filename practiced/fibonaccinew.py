reaching_value=int(input("Enter the reaching value "))
f1=1
f2=1
print('f1= ',f1)
print('f2= ',f2)
counter=3
while True:
	if f2<reaching_value:
		f3=f1+f2 
		counter+=1
		print(f"f{counter} = {f3}")
		f1=f2
		f2=f3
	else:
		print(f"The f{counter}'s value is the first reaching {reaching_value}")
		break	