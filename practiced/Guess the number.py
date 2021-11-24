print("Guess my number between 1-50. you have only 9 lives.")
l=9
print("What did you guess?\n")
while(l>=1):
	g=int(input())
	l=l-1
	if g==24 or g==25 or g==26  or g==27 or g==28 or g==29 or g==30:
		print("Lives remain = ",l,"\nyou have to lower the value.")
		continue
	if g==21 or g==22 or g==23:
		print("Lives remain = ",l,"\nYou are so close, decrease a little more.")	
		continue
	if g>30:
		print("Lives remain = ",l,"\nThis is too high, you have to lower more.")
		continue
	if g==19 or g==18 or g==17:
		print("Lives remain = ",l,"\nYou are so close, increase a little more.")
		continue
	if g==16 or g==15 or g==14 or g==13:
		print("Lives remain = ",l,"\nYou have to increase the value.")
		continue
	if g<13 :
		print("Lives remain = ",l,"\nThis is too low, you have to increase more.")
	if g==20:
		print("Congratulations! You guessed it right within ",9-l,"try/tries")
		break
	if l==0:
		print("Game Over! \n You lose, better luck next time.")	
		