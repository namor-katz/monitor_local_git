from tkinter import *


box = Tk()

list_5 = ['один', 'два', 'три', "четыре", "пять", 'шесть', "семь"]
i = 1
for elem in list_5:
    if i % 2 == 0:
        color = 'white'
    else:
        color = '#C0C0C0'
    i = i + 1
    label = Label(text=elem, bg=color)
    label.pack()

mainloop()
