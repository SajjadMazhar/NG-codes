

class Results:
	
	def __init__(self, all_results):
		self.all_results=all_results
		
	def show_result(self, requested_result):
		if requested_result in self.all_results:
			print("Your result is: ")
			print(self.all_results[str(requested_result)])
			if requested_result=='Samir':
				print('''
				$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				$$You are fucking amazing bro!!$$
				$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				''')	
			elif requested_result=='Naim':
				print('''
				Qualified!!''')
			elif requested_result=='Shahnawaz':
				print('''
				Qualified!!''')
				
	
class Student:
	
	def request_result(self):
		print("Enter your name to get your result: ")
		self.names=input()
		return self.names
		
				 
		
def main():
	a_results=Results({'Naim':['Reasoning: 50','English: 45','Quantitaive Aptitude: 40','General Intelligence: 40','Total: 175'],'Samir':['Reasoning: 50','English: 50','Quantitaive Aptitude: 50','General Intelligence: 50','Total: 200'],'Shahnawaz':['Reasoning: 40','English: 40','Quantitaive Aptitude: 40','General Intelligence: 40','Total: 160']})	
	student=Student()
	a_results.show_result(student.request_result())
		
main()		