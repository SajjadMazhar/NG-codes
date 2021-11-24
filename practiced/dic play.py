dic={':)':'😊'}
sent=input()
words=sent.split(' ')
cont=''
for word in words:
	cont=cont+dic.get(word,word)+' '
print(cont)
	

		
	