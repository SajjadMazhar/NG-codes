dic={'1':'one','2':'two','3':'three'}
num=input()
container=''
for i in num:
	container=container+ dic.get(i,'!!') + ' '
print(container)
	

		
	