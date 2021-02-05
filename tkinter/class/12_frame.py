import tkinter.messagebox as msgbox
from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="choose the menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

# 메뉴 프레임
frame_buger = Frame(root, relief="solid", bd=1)
frame_buger.pack(side="left",fill="both",expand=True)
Button(frame_buger, text="Hamburger").pack()
Button(frame_buger, text="cheezeburger").pack()
Button(frame_buger, text="chickenburger").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink, text="cola").pack()
Button(frame_drink, text="cider").pack()


root.mainloop()
