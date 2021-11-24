import time

story='''It’s as hard to have a favorite sequence of myths as it is to have a favorite
style of cooking (some nights you might want Thai food, some nights sushi,

other nights you crave the plain home cooking you grew up on). But if I had

to declare a favorite, it would probably be for the Norse myths.

My first encounter with Asgard and its inhabitants was as a small boy, no

more than seven, reading the adventures of the Mighty Thor as depicted by

American comics artist Jack Kirby, in stories plotted by Kirby and Stan Lee

and dialogued by Stan Lee’s brother, Larry Lieber. Kirby’s Thor was

powerful and good-looking, his Asgard a towering science fictional city of

imposing buildings and dangerous edifices, his Odin wise and noble, his Loki

a sardonic horn-helmeted creature of pure mischief. I loved Kirby’s blond

hammer-wielding Thor, and I wanted to learn more about him.

I borrowed a copy of Myths of the Norsemen by Roger Lancelyn Green

and read and reread it with delight and puzzlement: Asgard, in this telling,

was no longer a Kirbyesque Future City but was a Viking hall and collection

of buildings out on the frozen wastes; Odin the all-father was no longer

gentle, wise, and irascible, but instead he was brilliant, unknowable, and

dangerous; Thor was just as strong as the Mighty Thor in the comics, his

hammer as powerful, but he was . . . well, honestly, not the brightest of the

gods; and Loki was not evil, although he was certainly not a force for good.

Loki was . . . complicated.

In addition, I learned, the Norse gods came with their own doomsday:

Ragnarok, the twilight of the gods, the end of it all. The gods were going to

battle the frost giants, and they were all going to die.

Had Ragnarok happened yet? Was it still to happen? I did not know then.

I am not certain now.'''

words=story.split(' ')
for word in words:
	time.sleep(0.5)
	print(word,end=' ',flush=True)
	
	