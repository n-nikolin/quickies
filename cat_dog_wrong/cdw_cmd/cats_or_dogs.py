import os
import random
import time, sys

r = random.randint(0, 1)
u = int(input('Угадай, кошка или собака?\n"1" - кошка / "0" - собака: '))

def cat_or_dog(a):
	
	indent = 0 # How many spaces to indent
	indent_increasing = True # Whether the indentation is increasing or not
	
	try:
		while True: # The main program loop
			print(' ' * indent, end='')
			print(a)
			time.sleep(0.1) # Pause for 1/10 of a second
        
			if indent_increasing:
				# Increase the number of spaces
				indent = indent + 1
				if indent == 20:
					# Change direction
					indent_increasing = False
			
			else:
				# Decrease the number of spaces
				indent = indent - 1
				if indent == 0:
					# Change direction
					indent_increasing = True
	except KeyboardInterrupt:
		sys.exit()

def show_pic(f):
	path = f
	files=os.listdir(path)
	d=random.choice(files)
	os.startfile(path + '\\' + d)

if u==r:
	if r == 0:
		f = 'dogs'
		a = 'ПЁСЕЛЬ!!!'
		show_pic(f)
		cat_or_dog(a)
	else:
		f = 'cats'
		a = 'КИСЯЯ!!!!'
		show_pic(f)
		cat_or_dog(a)
else:
	a = 'НЕПРАВИЛЬНЫЙ ОТВЕТ!!!!'
	f = 'fu'
	show_pic(f)
	cat_or_dog(a)
