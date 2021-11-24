class Time:
	def __init__(self, hr, min):
		self.hr=hr
		self.min=min
	
	def addTime(self, t1_h=0, t2_h=0, t1_m=0, t2_m=0):
		total_hr = t1_h + t2_h
		total_min = t1_m + t2_m
	
		if total_min < 60:
			print(f"{total_hr} hr and {total_min} min")
		else:
			while total_min>60:
				total_min=total_min - 60
				total_hr= total_hr + 1
		print(f"{total_hr} hr and {total_min} min")		
				
time1=Time(2, 40)
time2=Time(1, 20)
time1.addTime(time1.hr, time1.min)
time2.addTime(time2.hr, time2.min)
