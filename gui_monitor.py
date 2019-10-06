#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# gui 

from tkinter import *
from monitor_g import *


box = Tk()


def refresh():
    fc = frame2.winfo_children()
    if len(fc) > 1:
        for lab in fc:
            #print(lab)
            lab.destroy()

    i = 0
    list_dirs = os.listdir(full_path)
    list_mutate = []
    #print('this len list_m ', len(list_mutate))
    for new_dir in list_dirs:
        if get_git_status(new_dir) is True:
            list_mutate.append(new_dir)
        else:
            pass

    print('this final lis_m ', len(list_mutate))
    for elem in list_mutate:
        if i % 2 == 0:
            color = 'white'
        else:
            color = '#C0C0C0'
        i = i + 1
        label = Label(frame2, text=elem, bg=color)
        label.pack()


button = Button(box, text="refresh", command=refresh, bg='green')
button.pack()

frame2 = Frame(box)
frame2.pack()

box.title('git monitor')
mainloop()
