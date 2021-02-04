from  tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text = "hello")
label1.pack()

photo = PhotoImage(file="C:\\Users\\kmkkm\\Desktop\\python_dev\\python_Gui\\gui_basic\\img.png")
label2 = Label(root, image = photo)
label2.pack()


def change():
    label1.config(text="see you again")
    
    global photo2
    photo2 = PhotoImage(file = "C:\\Users\\kmkkm\\Desktop\\python_dev\\python_Gui\\gui_basic\\img2.png")
    label2.config(image = photo2)


btn = Button(root, text = "click", command = change)
btn.pack()

root.mainloop()