word_to_guess = 'computer'
ellist=list(word_to_guess)
mlist=ellist.copy()
list=['?']*len(ellist)
print("You have four lives to guess the word letter by letter ")
lives=4
while(1):
	print(list)
	inlet=input("Entet the letter: ")

	if inlet in ellist:
		print("You guessed right")
		i=ellist.index(inlet)
		list[i]=inlet
		ellist[i]=0
		print(lives)
		if list==mlist:
			print("You win!")
			break
	elif inlet != ellist:
		print("You guessed wrong")
		lives-=1
		if lives==0:
			print("you lose!")
			break
		else:
			print(f"wrong choice! you have only {lives} lives left")
	
	