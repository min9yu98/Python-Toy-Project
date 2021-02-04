from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "Button2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "Button3")
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text = "Button4")
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", text = "Button5")
btn5.pack()

photo = PhotoImage(file="C:\\Users\\kmkkm\\Desktop\\python_dev\\python_Gui\\gui_basic\\img.png")
btn6 = Button(root, image = photo)
btn6.pack()


def btncmd():
    print("Button is working")

btn7 = Button(root, text = "WorkingButton", command=btncmd)
btn7.pack()

root.mainloop()