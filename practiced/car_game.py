print('''
write start - to start the car
write stop- to stop the car
write quit- to exit the program

''')
cond=''
while True:
	car=input('>')
	if car!=cond:
		if car=='start':
			print("The car is started")
			cond='start'
		elif car=='stop':
			print('The car is stopped')
			cond='stop'
		elif car=='quit':
			break
		else:
			print('I do not understand ')
	elif car==cond and cond=='start':
		print(f'car is already {cond}ed..!')
	elif car==cond and cond=='stop':
		print(f'car is already {cond}ped..!')
	