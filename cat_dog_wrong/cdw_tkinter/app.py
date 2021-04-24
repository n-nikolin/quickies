# A GUI app with two buttons
# for the retarded random cat, dog or wrong game
# Player takes a guess. If the player answers right
# A picture of a cat or a dog pops up
# And a sound effect plays. Same goes with wrong answers.

# TODO: add sfx
# TODO: make GUI look better
# TODO: add messageboxes
# TODO: add function to open random image from appropriate folder
# TODO: convert to .exe file to learn how it is done 

from tkinter import *
from tkinter import messagebox
import os, random

root = Tk()

def random_number():
	return random.randint(0, 1)

def btn_cat_click():
	x = 0
	win_lose(x)

def btn_dog_click():
	x = 1
	win_lose(x)

def win_lose(x):
	#
	r = random_number()
	if x == r:
		if x == 0:
			os.startfile('poop.jpg')
		if x == 1:
			os.startfile('doog.jpg')
		print('you win')
	else:
		os.startfile('fu.jpg')
		print('you lose!')

root['bg'] = '#7D53DE'
root.title('CAT, DOG or WRONG')
root.geometry('500x300')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=500)
canvas.pack()

frame = Frame(root, bg = '#34F6F2')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='сделай выбор', bg='#EEF8FF', font=40)
title.pack()

btn_cat = Button(frame, text='кiт', bg='yellow', command=btn_cat_click)
btn_cat.pack()
btn_dog = Button(frame, text='пес', bg='yellow', command=btn_dog_click)
btn_dog.pack()

root.mainloop()