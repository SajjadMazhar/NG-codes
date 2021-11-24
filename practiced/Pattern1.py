def pat(n,m):
	i=0
	if m==True:
		while(i<n):
			print((i+1)*str(int(n)))
			i=i+1
	if m==False:
		while(i<n):
			print((n-i)*str(int(n)))
			i=i+1
if __name__=='__main__':
	x=int(input("enter an integer\n"))
	log=int(input("Enter '1' for True or '0' for False\n"))
	y=bool(int(log))
	pat(x,y)
		