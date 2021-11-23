import random

question_list = [
                "In the following question, a word has been written in four different ways out of which onlyone is correctly spelt. Select the correctly spelt word" ,
                "A body of mass 8 kg is moving with a velocity of 4 m/s, find its momentum" ,
                "Which of these Indian athletes refused to accept the bronze medal awarded to her after a controversial bout in the Asian Games?" ,
                "In which American city is the famous indoor stadium Madison Square Garden located?" ,
                "Which of the following is called ‘falak’ in Arabic?" ,
                "Each fragment of the earth's crust is called a ___?___" ,
                "Which song did Kavi Pradeep compose to pay homage to the martyrs of the Indo-China war?" ,
                "The symbol of which arithmetic operation also resembles a letter of the English Alphabet?" ,
                "In the following question, select the missing number from the given series. 66, 65, 63, 62, 60,__ ?"

]


option_list = [
                ["Fallacoius", "Falacious", "Fallacious", "Fallacous"] ,
                ["32", "4" , "33" , "8"] ,
                ["Annu Rani" , "Shiva Thapa" , "L Sarita Devi" , "Devendra Singh Laishram"] ,
                ["San Francisco" , "New York City" , "Washington DC" , "Los Angeles"] ,
                ["Earth" , "Moon" , "Water", "Sky"] ,
                ["Slab" , "Plane" , "Plate" , "Platter"] ,
                ["Ab Tumhare Hawale Watan" , "Mere Desh ki Dharti" , "Apni Azadi Ko Hum" , "Aye Mere Watan ke Logon"] ,
                ["Addition" , "Multiplication" , "Division" , "Subtraction"] ,
                ["58" , "59" , "57" , "56"]
]

def lifeLine5050(opt, listToReduce):
    listOpt = listToReduce[opt]
    listToReduce.remove(listOpt)
    while True:
        randoms = random.choice(listToReduce)
        if randoms != listOpt:
            listToReduce.remove(randoms)
        if len(listToReduce) == 1:
            break
    return listToReduce[0]




answer_list = [2,0,2,1,3,2,3,1,1]
winning_amounts = [1000, 5000, 10000, 100000, 150000, 2500000, 5000000, 10000000, 50000000]
index = 0
lifeline_counter = 1
userName = input("Enter your name: ")
print("Welcome to the KBC game, "+userName+".")
while index < len(question_list):
    print(f"Question {index+1} for {winning_amounts[index]}\-")
    print(f'Q.{index+1}- {question_list[index]}')
    print("Your options are:")
    for i, option in enumerate(option_list[index]):
        print(f"{i+1}> {option}")
    print("\nEnter '5050' to use 50-50 lifeline if you want.")
    yourAns = int(input("Choose your option: "))
    
    if yourAns == 5050 and lifeline_counter < 1:
        print("Sorry, You can't use lifeline twice.\n")
        continue

    if yourAns-1 == answer_list[index]:
        youWin = winning_amounts[index]
        print("\n******CONGRATS******")
        print(f"you win {youWin}\-\n")
    elif yourAns == 5050:
        lifeline_counter -=1
        ansOpt = answer_list[index]
        option_list[index] = [option_list[index][ansOpt], lifeLine5050(ansOpt, option_list[index])]
        ans_index = option_list[index].index(option_list[index][0])
        answer_list[index] = ans_index
        continue
    else:
        print("You lose")
        break

    index+=1

