class student:
	def __init__(self,name,sub,fee):
		self.Name=name
		self.Subject=sub
		self.Monthly_fees=fee
	
	pass
	
s1=student("Naim","Physics and Maths",1000)
s2=student("Samir","Chemistry",500)
s3=student("Shahnawaz","English, Maths and Biology",1500)
print(s1.__dict__)
print(s3.Monthly_fees)