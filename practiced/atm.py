pin=1234
name="Sajjad Mazhar"
balance=10000
input_pin=int(input("Enter your pin: "))
print("Welcome", name, "\n")

while True:
	if input_pin==pin:
		choice=input("Press 1 to check balance.\nPress 2 to withdraw an amount.\nPress 3 to exit the program.\n>>> ")
		if choice=='1':
			print("Your current balance is Rs. ",balance,"\- only.\n")
		elif choice=='2':
			amount=int(input("Enter an amount to withdraw: "))
			if amount>balance:
				print(f"Sorry you can not withdraw this amount. You have only Rs. {balance}\- only in your account.\n")
			else:
				confirm=int(input("Enter 1 to confirm or 0 to stop withdrawal: "))
				if confirm==1:
					balance-=amount
					print("The amount withdrawn successfully...\nYour current balance is Rs. ", balance,"\- only\n")
				else:
					print("Transaction denied.\n")
					continue
		else:
			exit()