def fun(n):
	if n==0:
		return 1
	else:
		return n*fun(n-1)

m=int(input("enter m"))
r=int(input("enter r"))
ncr= fun(m)/(fun(r)*fun(m-r))
print(ncr)	