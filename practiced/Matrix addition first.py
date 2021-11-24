def matrix(m,n):
	for i in range(m):
		row=[]
		for j in range(n):
			inp=int(input(f"Enter Row {i+1} col {j+1} value = "))
			row.append(inp)
		col.append(row)
	return col
def add(A,B):
	for i in range(m):
		sumr=[]
		for j in range(n):
			sumr.append(A[i][j]+B[i][j])
		sumc.append(sumr)
	return sumc
print("enter order")
m=int(input())
n=int(input())
print("Enter elements in A")
col=[]
A=matrix(m,n)
print(col)
print("Enter elements in B")
col=[]
B=matrix(m,n)
print(col)
print("sum is \n")
sumc=[]
summation=add(A,B)
print(summation)