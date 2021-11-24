## finding the max in the list
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# greatest = numbers[0]
# for i in range(1,len(numbers)):
#     if greatest < numbers[i]:
#         greatest = numbers[i]

# print(greatest)

# ## second maximum 
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers[-2])

# ## reverse order list
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# for i in range(len(places)-1, -1, -1):
#     print(places[i])

## binary to decimal
# binary = int(input("Enter a binary number: "))
# size = len(str(binary))
# s = 0
# for i in range(len(str(binary))):
#     rem = binary%10
#     s = s+(rem*(2**i))
#     binary = binary//10
# print("Decimal for the given binary is: ", s)

## difference
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# not_in_second = []
# for i in list1:
#     if i not in list2:
#         not_in_second.append(i)
# print(not_in_second)

## report card
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]
# for year, mark_list in enumerate(marks):
#     list_len = len(mark_list)
#     total = 0
#     for mark in mark_list:
#         total+=mark
#     print(f"Average of {year+1} year - {int(total/list_len)}")

## total sum pairs
# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# sum_pairs = []
# for i in range(len(n)-1):
#     pair = []
#     for j in range(i+1, len(n)):
#         if n[i] + n[j] == number:
#             pair.append(n[i])
#             pair.append(n[j])
#     if pair:
#         sum_pairs.append(pair)
# print(sum_pairs)

## magic square ##
# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# square_len = len(magic_square)

# sum_diag1 = 0
# sum_diag2 = 0
# isMagic = True
# for i in range(square_len):
#     sum_rows = 0
#     sum_colums = 0
#     for j in range(square_len):
#         sum_rows+=magic_square[i][j]
#         sum_colums+=magic_square[j][i]

#     if sum_colums != sum_rows:
#         isMagic = False
    
#     sum_diag1+=magic_square[i][i]
#     sum_diag2+=magic_square[i][square_len - i - 1]
    
# if (sum_diag1 != sum_rows) or (sum_colums != sum_diag2):
#     isMagic = False
# print(sum_diag2, sum_diag1, sum_colums, sum_rows)

# print(isMagic)

## kitne admi the and aao jodein## 
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odds, evens = 0,0
# odd_sum, even_sum = 0,0
# for number in elements:
#     if number%2 == 0:
#         evens+=1
#         even_sum+=number
#     else:
#         odds+=1
#         odd_sum+=number
# print(f"odds: {odds}, evens: {evens}")
# print(f"odd sum: {odd_sum}, even sum: {even_sum}")
# print(f"odd average: {odd_sum/odds}, even average: {even_sum/evens}")


## count occurance
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# char_set = sorted(list(set(char_list)))
# chars_with_count = []
# for char in char_set:
#     chars_with_count.append([char, char_list.count(char)])
# print(chars_with_count)

# for i in range(len(chars_with_count)):
#     print(f"{chars_with_count[i][0]} - {chars_with_count[i][1]} times")

##Duplicates submission_type: Duplicates
# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# set_n = list(set(n))
# duplicates = []
# for element in set_n:
#     if n.count(element) > 1:
#         duplicates.append(element)

# print(duplicates)

## substring-nikalo
# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# print(mainStr.replace(subStr+" ", ""))

## palindrome or not
# word = input("Enter the word: ")
# word_list = list(word)
# isPalindrome = True
# for i in range(int(len(word_list)/2)):
#     if word_list[i] != word_list[len(word_list)-1-i]:
#         isPalindrome = False
# print(isPalindrome)


## kbc
question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
wrong = False
iterator = 0

while not wrong:
    print(question_list[iterator])
    print("options")
    for i, option in enumerate(options_list[iterator]):
        print(f"{i+1}. {option}")
    print("Your option: ")
    userInput = int(input())
    if userInput == solution_list[iterator]:
        print("Correct")
        iterator+=1
        if iterator == 3:
            print("You are the winner")
            break
        else:
            print("lets go for the next one!")
    else:
        print("wrong, You lose!")
        wrong = True
    







