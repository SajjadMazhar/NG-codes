class Exam():
	full_marks="Full marks is 100"
	exam_time="3 Hours.."
	pass
	
exam1=Exam()
exam2=Exam()

exam1.sub="Physics"
exam1.day="Monday"
exam1.time="11:00 AM."

exam2.sub="Mathematics"
exam2.day="Wednesday"
exam2.time="2:00 PM."

print(exam1.sub)
print(Exam().full_marks)
print(exam2.__dict__)
