#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#

from tkinter import *
from monitor_g import *
from tkinter import ttk # новыя, модныя


box = Tk()

i = 1
list_dirs = os.listdir(full_path)
list_mutate = []
for new_dir in list_dirs:
    if get_git_status(new_dir) is True:
        list_mutate.append(new_dir)
    else:
        pass

for elem in list_mutate:
    if i % 2 == 0:
        color = 'white'
    else:
        color = '#C0C0C0'
    i = i + 1
    label = Label(text=elem, bg=color)
    label.pack()

button = Button(text="refresh")
button.pack()

box.title('git monitor')
mainloop()
