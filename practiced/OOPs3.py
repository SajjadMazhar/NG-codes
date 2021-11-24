class Exam():
	full_marks="Full marks is 100"
	exam_time="3 Hours.."
	def __init__(self, subject, day, time):
		self.sub=subject
		self.day=day
		self.time=time
	pass
	
exam1=Exam("Physics", "Monday", "11:00 AM.")
exam2=Exam("Mathematics", "Wednesday", "2:00 PM.")
print(exam1.sub)
print(exam2.time)
print(exam1.__dict__)