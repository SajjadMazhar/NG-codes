list1=[]
n=int(input("Enter the number of elements you want in the list"))
for i in range(1,n+1):
	e=input("Enter the element")
	list1.append(e)
print(list1)
print("What type of comprehension you want to make??")
typ=input()
m=int(input("enter the number of integers you want"))
list2=[j for j in range(m) if j%2==0]
print(list2)