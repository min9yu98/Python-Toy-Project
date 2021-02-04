from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text = "choose the menu").pack()

burger_var = IntVar() # 여기에 int형으로 값 저장
btn_burger1 = Radiobutton(root, text = "Hamburger", value = 1, variable = burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text = "Cheezeburger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "Chickenburger", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = "choose the drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "cola", value = "cola", variable = drink_var)
btn_drink1.select() # 기본값으로 설정
btn_drink2 = Radiobutton(root, text = "cider", value = "cider", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거중에서 선택된 라디오 항목의 값(value)을 출력 
    print(drink_var.get()) # 음료수 값중 선택된 값 출력

btn = Button(root, text="order", command=btncmd)
btn.pack()


root.mainloop()