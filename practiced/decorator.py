def check(func):
	def inside(a,b):
		if b==0:
			return "can't divide by zero"
		func(a,b)
		
	return inside
		
def div(a,b):
	return a/b
	
d=check(div)	
print(d(2,0))

	
		
