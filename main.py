from tkinter import *
import random
import string

root = Tk()
root.resizable(width=False, height=False)
root.title("Password generator")
root.geometry('300x250')
text = Text(root, height=15, width=50)

def clean():
    text.delete('1.0', END)

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def password():
    for n in range(int(number_entry.get())):
        password = ''
        for i in range(int(length_entry.get())):
            password += random.choice(chars)
        text.insert(END, password + '\n')

GenButton = Button(text='Generate', command=password)
ClBurron = Button(text='Clean', command=clean)


root.mainloop()