
import random
user_score = 0
computer_score = 0
play_count = 0
print("LETS PLAY...STONE,PAPER,SIRROR")
opt = ["s", "p", "r"]

for i in range(11):
    play_count += 1
    computer_turn = random.choice(opt)
    user_turn = input("Choose your otpions:\n's' - Stone\n'p' - Paper\n'r' - Sissor\n-->")
    if user_turn == "s" or user_turn == "S":
        if computer_turn == "s":
            print("Ohhh,  it's a TIE..!")
        elif computer_turn == "p":
            user_score += 1
            print("Ahh..You WIN this time")
        else:
            computer_score += 1
            print("Yheee...You LOSE..!")
    elif user_turn == "p" or user_turn == "P":
        if computer_turn == "s":
            user_score += 1
            print("Ahh..You WIN this time")
        elif computer_turn == "p":
            print("Ohhh, it's a TIE...!")
        else:
            computer_score += 1
            print("Yhee...You LOSE..!")
    elif user_turn == "r" or user_turn == "R":
        if computer_turn == "s":
            computer_score += 1
            print("Yhee...You LOSE..!")
        elif computer_turn == "p":
            user_score += 1
            print("Ahh..You WIN this time")
        else:
            print("Ohhh, it's a TIE...!")
    else:
        print("Wrong input..! Try entering from the given options")

print("*" * 30)
if computer_score > user_score:
    print("LOSER....I win and you LOSE")
    print("Your score: " + str(user_score) +"\nMy score: " + str(computer_score))
elif computer_score < user_score:
    print("Ohh.. Shits.. You WIN...but i bet you win not win again")
    print("Your score: " + str(user_score) +"\nMy score: " + str(computer_score))
else:
    print("I am Shocked.. Ahhh... it's a TIE")