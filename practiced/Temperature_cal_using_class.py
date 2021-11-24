class Temp:
	
	def c_to_f(self, c_temp):
		fahrenheit=((9/5)*c_temp) + 32
		return fahrenheit
		
	def f_to_c(self, f_temp):
		celcius=5*(f_temp - 32)/9
		return celcius
		
temp=Temp()
choice=input("Enter 'F' to input in Fahrenheit or 'C' to input Celcius: ")
if choice=='F' or choice=='f':
	input_temp=int(input(f"Enter the temperature in {choice}: "))
	temp.temperature=input_temp
	print("The temperature in Celcius is: ", temp.f_to_c(temp.temperature))
elif choice=='C' or choice=='c':
	input_temp=int(input(f"Enter the temperature in {choice}: "))
	temp.temperature=input_temp
	print("The temperature in Fahrenheit is: ", temp.c_to_f(temp.temperature))
else:
	print("Your input is invalid!")


