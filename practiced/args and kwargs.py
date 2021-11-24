def fun(self,*args,**kwargs):
	print(args[1])
	print(self)
	print("these are my friends\n")
	for thing in y:
		print(thing)
	for i,j in kwargs.items():
		print(f"{i} mera {j} hai")
		
f=["sajjad","mazhar","imam"]
y=["ghulam","tanvir","aslam","tausif","samina"]
my="I am a student of final year B.Sc. and expected to graduate in 2020"
log={"ghulam":"bhai","tanvir":"dost","aslam":"baadiwala"}
fun(my,*f,*y,**log)