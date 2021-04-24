from tkinter import *
from tkinter import messagebox

root = Tk()

def btn_click():
    login = login_input.get()
    password = pass_field.get()
    
    info_str = f'Your data: {str(login)}, {str(password)} has been sent to the FBI'
    messagebox.showinfo(title='Название', message=info_str)

    #tk.messagebox.showerror(title='', message='ИДИнахуй!')

root['bg'] = '#fafafa'
root.title('еблявпопу')
root.geometry('666x666')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=666, width=666)
canvas.pack()

frame = Frame(root, bg = '#34F6F2')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='сделай выбор', bg='#EEF8FF', font=40)
title.pack()
btn = Button(frame, text='кiт', bg='yellow', command=btn_click)
btn.pack()

login_input = Entry(frame, bg='white')
login_input.pack()

pass_field = Entry(frame, bg='white', show='A')
pass_field.pack()

root.mainloop()