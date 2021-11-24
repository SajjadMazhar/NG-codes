class Exam():
	full_marks="Full marks is 100"
	exam_time_duration="3 Hours.."
	def details(self):
		return f"Subject is {self.sub}, exam day is {self.day}, exam starts at {self.time}"
	pass
exam1=Exam()
exam2=Exam()
exam1.sub="Physics"
exam1.day="Monday"
exam1.time="11:00 AM."

exam2.sub="Mathematics"
exam2.day="Wednesday"
exam2.time="2:00 PM."

print(Exam().exam_time_duration)
print(exam2.details())