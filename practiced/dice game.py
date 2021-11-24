import random
print("THIS IS A THREE PLAYER GAME. THE ONE WHO GET GREATER NUMBER BETWEEN 1 AND 6 WILL BE THE WINNER!!\n")
p1=input("ENTER your name player 1\n")
p2=input("ENTER your name player 2\n")
p3=input("ENTER your name player 3\n")
s1=0
s2=0
s3=0
round=0
index=10
while(index>0):
	round=round+1
	print(f"ROUND {round}\n")
	print(f"{p1}'s turn.")
	input("Press enter to roll the dice!")
	dice_1=random.randint(1,6)
	print(f"You got {dice_1}\n")
	print(f"{p2}'s turn.")
	input("Press enter to roll the dice!")
	dice_2=random.randint(1,6)
	print(f"You got {dice_2}\n")
	print(f"{p3}'s turn.")
	input("Press enter to roll the dice!")
	dice_3=random.randint(1,6)
	print(f"You got {dice_3}\n")
	if dice_1>dice_2:
		if dice_1>dice_3:
			print(f"{p1} wins!!")
			s1+=1
			index=index-1
			print("Score = +1\n")
		else:
			print(f"{p3} wins!!")
			s3+=1
			index=index-1
			print("Score = +1\n")
	else:
		if dice_2>dice_3:
			print(f"{p2} wins!!")
			s2+=1
			index=index-1
			print("Score = +1\n")
		else:
			print(f"{p3} wins!!")
			s3+=1
			index=index-1
			print("Score = +1\n")
			
print(f"The final score.\n{p1} = {s1}\n{p2} = {s2}\n{p3} = {s3}\n")
if s1>s2 and s1>s3:
	print(f"*****{p1} wins with score {s1}*****")
if s2>s1 and s2>s3:
	print(f"*****{p2} wins with score {s2}*****")
if s3>s1 and s3>s2:
	print(f"*****{p3} wins with score {s3}*****")	