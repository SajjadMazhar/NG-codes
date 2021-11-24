## Question 1
# number = int(input("Enter an integer greater than three digit: "))
# number = number//10
# print(number%100)

## question 2 doesnt work for duplicate characters in the string
# string = input("Enter a string: ")
# size = string.index(string[-1]) + 1
# print(size)

## palindrome
# word = input("Enter the word: ")
# word_list = list(word)
# isPalindrome = True
# for i in range(int(len(word_list)/2)):
#     if word_list[i] != word_list[len(word_list)-1-i]:
#         isPalindrome = False
# print(isPalindrome)

# pyramid with odd numbers
# userInput = int(input("Enter integer: "))
# for i in range(1, userInput, 2):
#     for j in range(userInput, i, -1):
#         print(" ", end="")
#     for k in range(0, i):
#         print(str(i)+" ", end="")
#     print("")
# for i in range(1,userInput+1):
#     print(f"{2*i-1}"*(2*i-1))

## special characters in between letters of a string
# string = "sajjadmazhar"
# spChar = "@"
# newString = ""
# for char in string:
#     newString=newString+char+spChar
# print(newString,newString[:len(newString)-1])

## fibonacci series
# n = int(input("enter the number of terms: "))
# a = 0
# b = 1
# print(a)
# for i in range(10):
#     c = a + b
#     print(c)
#     a = b
#     b = c

## finding missing numbers in between elements
# givenList = [1, 6, 9, 12]
# missing_nums = []
# for i in range(len(givenList)-1):
#     missing_nums.extend(list(range(givenList[i]+1, givenList[i+1])))
# print(missing_nums)

## angstrom number
# number = int(input("Enter input: "))
# exp = 3
# if len(str(number)) > 3:
#     exp = len(str(number))
# s=0
# for i in range(len(str(number))):
#     s+=int(str(number)[i])**exp
# if number == s:
#     print("Yes")
# else:
#     print("no")

## snake pattern with one loop
# n = int(input("Enter an integer: "))
# initial_num = 1
# for i in range(1, n+1):
#     if i%2 != 0:
#         for j in range(n):
#             print(str(initial_num)+" ", end="")
#             initial_num+=1
#     else:
#         for j in range(n+initial_num-1, initial_num-1, -1):
#             print(str(j)+" ", end="")
#             initial_num+=1
#     print()

## pascal triangle
# rows = int(input())
# pascal_list = []
# for i in range(rows):
#     temp_list = []
#     for j in range(i+1):
#         if j == 0 or j == i:
#             temp_list.append(1)
#         else:
#             temp_list.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
#     pascal_list.append(temp_list)
# print(pascal_list)
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(" ", end="")
#     for k in range(i+1):
#         print(pascal_list[i][k], end=" ")
#     print()


## horizontal pyramid with numbers
# # with two loops
# n = 5
# for i in range(n): #counter0
#     print(f"{i+1}"*(i+1))
# for j in range(n-1, 0, -1):
#     print(f"{j}"*(j))
# ##with one loop
# n = 5
# counter = 1
# while True:
#     if counter <= 5:
#         print(counter*str(counter))    
#     if n<=5 and counter > 5:
#         print((n-1)*str(n-1))
#         n-=1
#     if counter == 10:
#         break
#     counter+=1

## armstrong number
# userInput = int(input("Enter an integer: "))
# summation = 0
# for num in str(userInput):
#     summation+=int(num)**3
# if summation == userInput:      
#     print(True)
# else:
#     print(False)

# factorial
# def fact(n):
#     if n==0:
#         return 1
#     return fact(n-1)*n

# n = 5
# for i in range(n):
#     for j in range(n-i+1):
#         print(end=" ")
#     for j in range(i+1):
#         print(fact(i)//(fact(j)*fact(i-j)), end=" ")
#     print()

## biggest in list
# numbers = [1,2,44,33,22,53,45]
# big = numbers[0]
# for i in range(len(numbers)-1):
#     for j in range(1, len(numbers)):
#         if numbers[i] > numbers[j]:
#             big = numbers[i]
        
# print("sorted: ", big)

# bubble sort
# numbers = [1,2,44,33,22,53,45]
# for i in range(len(numbers)):
#     for j in range(1, len(numbers)-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(numbers)

## flat list
# nestedList = [1, 2, [3,4], [5,6]]
# flatList = []
# for i in nestedList:
#     if type(i) == type([]):
#         for j in i:
#             flatList.append(j)
#     else:
#         flatList.append(i)
# print(flatList)

## odd even list
# j = 0
# finalList = []
# n = int(input("Enter integer: "))
# for i in range(n+1):
#     if j < n//2:
#         finalList.append(2*i+1)
#         j+=1
#     else:
#         if 2*i - 100 == 0:
#             continue
#         finalList.append(2*i - n)
# if 0 in finalList:
#     finalList.remove(0)
# print(finalList)


# l = [1,2,3,4,5,4,7,9,2,0,4,7]
# for i in l.copy():
#     l.pop()
# print(l)

# set= {1, 4,  1.5, 6, 3+1j, 'sat', False, 'mahi', 1.02,(1,2,3)}
# print(set)


# l = [1,2,3,4,5]
# i=0
# while True:
#     l.remove(i)
#     if l==[]:
#         break
# print(l)

######################## 16 / 11 /2021 Tuesday #####################

# # binary to decimal and vice versa
# def to_decimal(bin):
# 	sbin=str(bin)
# 	blen=len(sbin)
# 	sum=0
# 	for i in range(0,blen):
# 		n=bin%10
# 		bin=bin//10
# 		sum=sum+n*(2**i)
# 	print("The decimal of the given binary is:",sum)
	
# def to_binary(dec):
# 	rem=dec%2
# 	bin=str(rem)
# 	dec=dec//2
# 	while(dec>0):
# 		rem=dec%2
# 		bin=str(rem)+bin
# 		dec=dec//2
# 	print("Binary of the given decimal is:",bin)

# choose=input("Enter D to calculate dec to bin, or B to calculate bin to dec!\n")
# if choose=='D' or choose =='d':
# 	dec=int(input("enter a decimal value: "))
# 	to_binary(dec)	
# elif choose=='b' or choose =='B':
# 	bin=int(input("Enter a binary: "))
# 	to_decimal(bin)


# question 1 print all odd and even
# j = 0
# for i in range(101):
#     if j < 50:
#         print(2*i+1)
#         j+=1
#     else:
#         if 2*i - 100 == 0:
#             continue
#         print(2*i - 100)

# question 2 multiplication table in list
# number = int(input("Enter a number: "))
# tableList = []
# for i in range(1, number+1):
#     tableList.append(i)
#     nestList = []
#     for j in range(1,11):
#         multiplyer = i*j
#         nestList.append(multiplyer)
#     tableList.append(nestList)
# print(tableList)
# with one loop i have to do this things

# # hangman
# from random import choice
# list_of_words = ["Sparrow", "Piano", "Physics", "Elephant"]
# list_of_hints = ["Bird", "Musical instrument", "Science related", "Animal"]
# hangMan = [
#     """
#     |
#     |
#     |
#     |
#     |
#     """,
#     """
#     |----
#     |
#     |
#     |
#     |
#     """,
#     """
#     |----
#     |   |
#     |
#     |
#     |
#     """,
#     """
#     |----
#     |   |
#     |   O
#     |  
#     |  
#     """,
#     """
#     |----
#     |   |
#     |   O
#     |  /|\\
#     |  
#     """,
#     """
#     |----
#     |   |
#     |   O
#     |  /|\\
#     |  / \\
#     """
# ]
# word_to_guess = choice(list_of_words)
# ind = list_of_words.index(word_to_guess)
# hint = list_of_hints[ind]
# ellist=list(word_to_guess.lower())
# mlist=ellist.copy()
# list=['?']*len(ellist)
# guessed = False
# print("You have four lives to guess the word letter by letter ")
# print(f"Hint: {hint}")
# lives=0
# while not guessed:
# 	print(list)
# 	inlet=input("Entet the letter: ")

# 	if inlet in ellist:
# 		print("You guessed right")
# 		i=ellist.index(inlet)
# 		list[i]=inlet
# 		ellist[i]=0
# 		print(lives)
# 		if list==mlist:
# 			print("You win!", mlist)
# 			guessed = True
# 	elif inlet != ellist:
# 		print(hangMan[lives])
# 		lives+=1
# 		if lives==6:
# 			print("you lose!")
# 			break
# 		else:
# 			print(f"wrong choice! you have only {lives} lives left")



# question 3 occurance
# number = int(input("Enter an integer: "))
# method1
# output = ''
# for char in sorted(str(number)):
#     output+=char
# print(output)
# method2
# numberList = list(str(number))

# for i in range(len(numberList)-1):
#     for j in range(1, len(numberList)):
#         if numberList[i] > numberList[j]:
#             numberList[i], numberList[j] = numberList[j], numberList[i]
# print(numberList)


## anagram
# word1, word2 = input("Enter first word: "), input("Enter second word: ")
# method1
# if sorted(word1) == sorted(word2):
#     print(True)
# else:
#     print(False)
# method2:
# counter = 0
# if len(word1) == len(word2):
#     for char in word1:
#         if char in word2 and word1.count(char)==word2.count(char):
#             counter+=1
#     if counter == len(word1):
#         print(True)
#     else:
#         print(False)

# swap key and value from a dictionary
# dic = {
#     "name":"Ujwal",
#     "age":60,
# }
# # with another dictionary
# newDic = {}
# for key in dic:
#     newDic[dic[key]] = key
# print(newDic)
# # without another dictionary
# for key in dic.copy():
#     dic[dic[key]] = key
#     print(dic)
#     del dic[key]
# print(dic)

# # print [-1,2,-3,4,-5,....,n]
# def change(n):
#     if n % 2 == 0:
#         return n
#     return n*(-1)
# method 2
# print([(-i) if i%2 != 2 else i for i in range(1, int(input("Enter:")))])

# print([change(a) for a in range(1,10)])


# # remove duplicates entirely from a list
# list_of_nums = [1,2,1,5,3,6,2]
# set_of_nums = list(set(list_of_nums))
# for element in set_of_nums:
#     count_of_element = list_of_nums.count(element)
#     if count_of_element > 1:
#         for i in range(count_of_element):
#             list_of_nums.remove(element)
# print(list_of_nums)

## empty a list without clear method
# this_list = [3,2,4]
# for i in range(len(this_list.copy())):
#     this_list.pop()
# print(this_list)
#method 2
# for i in range(len(this_list.copy())):
#     del this_list[0]
# print(this_list)
# method 3
# del this_list[:]
# method 4
# this_list*=0

# print(this_list)



## make an append function without using append
# def myAppend(l, element):
#     return l+[element]

# myList = [2,4,6]
# inp = int(input())
# print(myAppend(myList,inp))


## removing substring from astring
# string = 'sajjad'
# whichOne = int(input("Enter position: "))
# newStr = ''

# for i in range(len(string)):
#     if i == whichOne:
#         continue
#     else:
#         newStr+=string[i]
# print(newStr)

## what datatypes a set will accept and why?
# print({'string', True, 2+3j, 3.4, [4,3]})
# [3,4,5].__hash__() <-- willgive error because lists are mutable


## asci values
# inpString = input("")
# for char in inpString:
#     print(f"ASCII value for '{char}' is {ord(char)}\n")

# alphabet pattern
# string = "SAJJAD"
# newStr = ""
# endStr = ""
# print(string)
# for i in range(len(string)-1):
#     endStr += string[i]
#     newStr+=string[i+1: len(string)] +endStr + "\n"
        
# print(newStr)

## LCM
# a, b = int(input("enter first numeber: ")), int(input("enter second number: "))
# if a>b:
#     a,b = b,a
# p = a*b
# while True:
#     remainder = a%b
#     if remainder !=0:
#         a = b
#         b = remainder
#     else:
#         print("The HCF is ", b)
#         print("LCM is", p/b)
#         break

## 12h to 24h clock

# def timeConversion(s):
#     hour = s[:2]
#     minute = s[3:5]
#     seconds = s[6:8]
#     ampm = s[8:]
#     if ampm == "PM":
#         if int(hour) > 0:
#             hour =  int(hour) + 12

#     print(hour)
# timeConversion("01:33:43PM")
        
## kbc
# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]
# 2
# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1]
# wrong = False
# iterator = 0

# while not wrong:
#     print(question_list[iterator])
#     print("options")
#     for i, option in enumerate(options_list[iterator]):
#         print(f"{i+1}. {option}")
#     print("Your option: ")
#     userInput = int(input())
#     if userInput == solution_list[iterator]:
#         print("Correct")
#         iterator+=1
#         if iterator == 3:
#             print("You are the winner")
#             break
#         else:
#             print("lets go for the next one!")
#     else:
#         print("wrong, You lose!")
#         wrong = True

## pyramid pattern 2
# n = 4
# p = 1
# c = 1
# for x in range(1, n+1):
#     for y in range(n-1, x-1, -1):
#         print(" ", end="")
#     p=1
#     print(p, end="")

#     while c<x:
#         p+=1
#         print(p, end="")
#         c+=1

#     while c>1:
#         p//=2
#         print(p, end="")
#         c-=1
#     print()

# a = [7,6,5,4,3,3,3]
# for i in a:
#     if i in a and a.count(i) != 1:
#         a.remove(i)
#         if a.count(i)>1:
#             a.remove(i)
# print(a)

# multiplying three numbers without using * operator
# a, b, c, s, s2 = int(input("first: ")), int(input("second: ")), int(input("third: ")), 0, 0
# with two loops 
# for i in range(a):
#     s+=b
# for j in range(c):
#     s2 +=s
# print(s2)

# with one loop
# while True:
#     if a>0:
#         s += b
#         a-=1
#     else:
#         s2+=s
#         c-=1
#     if c<1:
#         break
# print(s2)

# a = [3,4,8,4,6]
# for i in a:
#     a.pop()
# print(a)
## the above code outputs [3,4] because every time the loop iterates it get reduced by one element 

## list to object
# detailList = [['Sajjad', 23, 'kolkata'], ['Ujjwal', 22, 'Bihar'],["Raja", 18, 'Bihar']]
# studentsObj = {}
# for index, details in enumerate(detailList):
#     detailsObj = {"name":'', "age":'', "location":''}
#     counter = 0
#     for key in detailsObj:
#         detailsObj[key] = details[counter]
#         counter+=1
#     studentsObj[f"student-{index+1}"] = detailsObj
# print(studentsObj)

## input 'sajjad' output {s:1, a:2, j:2, d:1}
# userString = input("Enter string: ")
# myObj = {}
# for char in userString:
#     charCount = userString.count(char)
#     if char not in myObj:
#         myObj[char] = charCount
# print(myObj)


## roman neumeral
# I, V,  X,  L,  C,   D,    M
# 1, 5, 10, 50, 100, 500, 1000 
# num = int(input("Enter an integer: "))
# roman = ''
# while num > 0:
#     if num < 4:
#         roman+='I'
#         num-=1
#     elif num == 4:
#         roman += 'IV'
#         num-=4
#     elif num >=5 and num < 9:
#         roman += 'V'
#         num-=5
#     elif num == 9:
#         roman += "IX"
#         num -= 9
#     elif num >= 10 and num< 40:
#         roman += "X"
#         num-=10
#     elif num >= 40 and num < 50:
#         roman+='XL'
#         roman -=40
#     elif num >=50 and num < 90:
#         roman+='L'
#         num-=50
#     elif num >=90 and num < 100:
#         roman +="XC"
#         num-=90
#     elif num >= 100 and num < 400:
#         roman = 'C'
#         num-=100
#     elif num >= 400 and num < 500:
#         roman += "CD"
#         num-=400
#     elif num >= 500 and num<900:
#         roman += 'D'
#         num -= 500
#     elif num>=900 and num<1000:
#         roman+="CM"
#         num-=900
#     elif num >= 1000:
#         roman='M'
#         num-=1000
#     else:
#         num-=1
# print(roman)

## multiplication table with lambda function
# multiplyers = list(range(1,11))
# num = int(input("Enter num:"))
# table = list(map(lambda n : n*num, multiplyers))
# print(table)

## function theory

## flatten list with recursion
# def flatening(nested):
#     for i in nested:
#         if type(i) == type([]):
#             flatening(i)
#         else:
#             flatList.append(i)

# nestedList = [1, 2, [3,4], [5,6],[3,[3,2,[4,0]]]]
# flatList = []
# flatening(nestedList)
# print(flatList)

## fibonacci 
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(int(input("Enter number of elements: "))):
#     print(fib(i))

## print with recursion
# 1
# 22
# 333
# 4444
# 55555
# def pattern(n):
#     if n > 5:
#         return
#     print(str(n)*n)
#     pattern(n+1)
#     print(str(n-1)*(n-1))

# pattern(0)
