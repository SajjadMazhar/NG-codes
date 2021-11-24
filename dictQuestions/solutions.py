

## question 2
# dict={"name":"Raju", "marks":56}
# key = input("enter key: ")
# if key in dict:
#     print("exist")
# else:
#     print("does not exist")

# question 3
# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 
# s = 0
# for i in my_dict:
#     s+=my_dict[i]
# print(s)

## question 4
# Dic= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#           3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#             }
#         }
# del Dic[3]['A']
# print(Dic)

## question 5
# list1=['one','two','three','four', 'five']
# list2=[1,2,3,4,5,] 
# dic = {}
# for i in range(len(list1)):
#     dic[list1[i]] = list2[i]

# print(dic)

## question 6
# dic={
#     'ball':'red',
#     'bat':4,
#     'wickets':8,
#     'ball':'green',
#     'bat':3
#     }
# newDic = {}
# for i in dic:
#     if i not in newDic:
#         newDic[i] = dic[i]
# print(newDic)

## question 7
# n =  [
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ]
# outputList = []
# for i in n:
#     for j in i:
#         if i[j] not in outputList:
#             outputList.append(i[j])
# print(outputList)

## question 8
# name = input("enter name: ")
# marks = int(input("enter marks"))
# marksheet = {}
# marksheet[name] = marks

## question 9
# string = "MISSIISSIPPI"
# set_list = set(list(string))
# dic = {}
# counter = 0
# for char in set_list:
#     dic[char] = string.count(char)
# print(dic)

## question 10
# dic =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# s = 0
# for key in dic:
#     s += len(dic[key])

# print(s)

## question 11
# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# nums = [my_dict[x] for x in my_dict]
# nums = sorted(nums)
# highest_3 = []
# for i in range(-1, -4, -1):
#     highest_3.append(nums[i])
# print(highest_3)

## question 12
# dic = {}
# for i in range(1,16):
#     dic[i] = i**2
# print(dic)

## question 13
# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     }
# highest = my_dict['a']
# my_dict.
# for key, value in my_dict.items():

## question 14
# dic = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# numbers = []
# for name in dic:
#     numbers.append(dic[name])
# numbers = sorted(numbers)
# max_3 = []
# for i in range(-1, -4, -1):
#     max_3.append(numbers[i])
# max_3keys = []
# for name in dic:
#     if dic[name] in max_3:
#         max_3keys.append(name)
# print(max_3keys)

##




    