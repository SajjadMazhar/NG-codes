import time
print("This is excercise program")
ct=time.asctime(time.localtime(time.time()))
water_in=time.time()
phy_in=time.time()
eye_in=time.time()
watert=10
phyt=50
eyet=80
def water():
	print("Drink water and rest for 5 minutes\n")
	drank=int(input("Enter 1 if you have done it = "))
	f=open("file.txt","a")
	f.write("Water Drank. ")
	f.write(ct)
	f.write("\n")
	f.close()
def eye():
	print("do eye exercise\n")
	done=int(input("Enter 1 if you have done it = "))
	f=open("file.txt","a")
	f.write("eyes done. ")
	f.write(ct)
	f.write("\n")
	f.close()
def phy():
	print("do phy exercise\n")
	done=int(input("Enter 1 if you have done it = "))
	f=open("file.txt","a")
	f.write("Phy. exercise done. ")
	f.write(ct)
	f.write("\n")
	f.close()
while(True):
	if time.time()-water_in > watert:
		water()
		water_in=time.time()		
	if time.time()-phy_in> phyt:
		phy()
		phy_in=time.time()
	if time.time()-eye_in> eyet:
		eye()
		eye_in=time.time()