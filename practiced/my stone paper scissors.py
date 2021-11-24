#stone paper scissors game
import random
score_my=0
score_com=0
round=10
list=["st","pp","sc"]
print("Enter 'st' for stone, 'pp' for paper or 'sc' for scissors.")

while(round>0):
	print(f"Round- {11-round}")
	com_ch=random.choice(list)
	my_ch=input("You choose: ")
	if com_ch=="st" and my_ch=="pp":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: okay you win this time\n")
		score_my=score_my + 1
		round=round - 1
	elif com_ch=="st" and my_ch=="sc":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: yeahh!! you lose.....!!\n")
		score_com=score_com + 1
		round=round - 1
	elif com_ch=="st" and my_ch=="st":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: Now its a tie, lets play again!\n")
		round=round - 1	
	elif com_ch=="pp" and my_ch=="pp":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: Now its a tie, lets play again!\n")
		round=round - 1
	elif com_ch=="pp" and my_ch=="sc":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: okay you win this time\n")
		score_my=score_my + 1
		round=round - 1
	elif com_ch=="pp" and my_ch=="st":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: yeahh!! you lose.....!!\n")
		score_com=score_com + 1
		round=round - 1
	elif com_ch=="sc" and my_ch=="pp":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: yeahh!! you lose.....!!\n")
		score_com=score_com + 1
		round=round - 1
	elif com_ch=="sc" and my_ch=="sc":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: Now its a tie, lets play again!\n")
		round=round - 1
	elif com_ch=="sc" and my_ch=="st":
		print("Jarvis chooses: ",com_ch)
		print("Jarvis: okay you win this time\n")
		score_my=score_my + 1
		round=round - 1
if score_my>score_com :
	print("""
 	CONGRATULATIONS!!
	YOU WON.
	""")
	
	
elif score_my<score_com: 
	print("""
		YOU LOSE!
	""")
	
else:
	print("""
		IT IS A TIE. LET'S PLAY A TRY BREAKER ROUND!
	""")

print("\nYour score: ",score_my,"\nJarvis' score",score_com)
		