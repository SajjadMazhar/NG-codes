condition=True
print("""
start-start the car
stop-stop the car
quit-quit the program""")
inp_condition=input(">").lower()
while condition:
	if inp_condition=='start':
		print('car is started')
		inp_condition='started'
	elif inp_condition=='stop':
		print('car has stopped')
		inp_condition='stopped'
	elif inp_condition=='quit':
		print('successfully exited')
		
	if inp_condition=='started' or inp_condition =='stopped':
		if inp_condition=='started':
			print('already started')
		elif inp_condition=='stopped':
			print('already stopped')
	inp_condition=input('>')
	
		
	