from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar() # chkvar에 int형으로 값을 저장한다
checkbox = Checkbutton(root, text="Don't watch today", variable = chkvar)
# checkbox.select() # 자동선택처리
# checkbox.deselect() # 선택해지처리
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = "Don't watch week", variable = chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크해제 1: 체크
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()