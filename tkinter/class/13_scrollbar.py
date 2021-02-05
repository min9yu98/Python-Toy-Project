from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set)
for line in range(1, 51):
    mylist.insert(END, str(line))
mylist.pack(side=LEFT)
scrollbar.config(command=mylist.yview)
mainloop()
