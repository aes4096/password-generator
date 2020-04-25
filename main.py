from tkinter import *
import random
import string

root = Tk()
root.resizable(width=False, height=False)
root.title("Password generator")
root.geometry('420x340')
text = Text(root, height=15, width=50)

def clean():
    text.delete('1.0', END)

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def password():
    text.delete('1.0', END)
    for n in range(int(number_entry.get())):
        password = ''
        for i in range(int(length_entry.get())):
            password += random.choice(chars)
        text.insert(END, password + '\n')

GenButton = Button(text='Generate', command=password)
ClButton = Button(text='Clean', command=clean)

number_entry = Entry(width=10, justify=CENTER)
length_entry = Entry(width=10, justify=CENTER)
number_entry.insert(0, '')
length_entry.insert(0, '')

number_label = Label(text="      Количество паролей")
length_label = Label(text="      Длина пароля")
number_label.grid(row=0, column=0, sticky="w")
length_label.grid(row=1, column=0, sticky="w")
number_entry.grid(row=0, column=1, padx=1, pady=5)
length_entry.grid(row=1, column=1, padx=1, pady=5)

GenButton.grid(row=2, column=0, padx=5, pady=5, sticky="e")
ClButton.grid(row=2, column=2, padx=15, pady=5, sticky="w")
text.grid(row=4, column=0, sticky='nsew', columnspan=3)

scrollb = Scrollbar(root, command=text.yview)
scrollb.grid(row=4, column=4, sticky='nsew')
text.configure(yscrollcommand=scrollb.set)

root.mainloop()