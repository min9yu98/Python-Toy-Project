from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#여러줄
txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "input")

#한줄 (ex:로그인같은 것)
e = Entry(root, width=30)
e.pack()
e.insert(0, "input")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1: 첫번째라인 , 0: 0번재 column위치 
    print(e.get())
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()