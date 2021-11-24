##  Write a Python program to calculate the sum of a list of numbers
# def sumList(numList):
#     size = len(numList)
#     if size == 1:
#         return numList[0]
#     return numList[0] + sumList(numList[1:])
# method2

## printing counting numbers
# def counter(i):
#     if i == 0:
#         return
#     counter(i-1)
#     print(i)

# counter(5)
        

# numList = [2,4,5,6,8]
# print(sumList(numList))

## factorail of a number
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)

# number = int(input("Enter an integer: "))
# print(fact(number))

## Write a Python program to convert an Integer to a string in any base

## fibonacci 
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(10):
    # print(fib(i))

## printing number in words
# words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# def convert(n, arr):
#     if n==0:
#         return
#     convert(n//10, arr)
#     print(words[n%10])

# convert(342, words)

## exponents
# def power(m, n):
#     if n == 0:
#         return 1
#     return m*power(m, n-1)

# print(power(2,3))

## sorted or not
# def isSorted(arr, i):
#     if i>= len(arr):   
#         return True
#     if arr[i] < arr[i-1]:
#         return False
#     return isSorted(arr, i+1)

# print(isSorted([2,3,4,5,6], 1))

# def fun(x):
     
#     if(x > 0):
#         x -= 1
#         fun(x)
#         print(x , end=" ")
#         x -= 1
#         fun(x)
#     return
         
# a = 10
# fun(a)

## max in array
# def fun( a, n):
#     if(n == 1):
#         return a[0]
#     else:
#         x = fun(a, n - 1)
#     if(x > a[n - 1]):
#         return x
#     else:
#         return a[n - 1]

# arr = [12, 10, 30, 200, 50, 100]
# print(fun(arr, 5))
 
# # binary with recursion
# def convert(n):
#     if n == 0:
#         return 

#     convert(n//2)
#     print(n%2, end="")
# convert(4)
# print()