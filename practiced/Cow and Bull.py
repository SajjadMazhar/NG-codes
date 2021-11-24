print("Welcome to Cow and Bull game.\nYou have to guess a 4 digit number.\nFor every right guess you get a Cow and Bull for wrong guess.")
num=[1,2,3,4]
while(1):
	c=0
	b=0
	n=int(input("Guess The NUMBER!\n"))
	n4=n%10
	n=n//10
	n3=n%10
	n=n//10
	n2=n%10
	n=n//10
	n1=n%10
	if n1==num[0]:
		c=c+1
	else:
		b=b+1
	if n2==num[1]:
		c+=1
	else:
		b+=1
	if n3==num[2]:
		c+=1
	else:
		b+=1
	if n4==num[3]:
		c+=1
	else:
		b+=1
	if c==4 and b==0:
		print("You Guessed the right number...")
		break
	else:
		print(f"You got {c} Cow(s) and {b} Bull(s)\n")
		print("Press 'e' to exit or 'r' to try again")
		er=input()
		if er=='e' or er=='E':
			print("Successfully exited the programme.... ..")
			break
		elif er=='r' or er=='R':
			continue
	