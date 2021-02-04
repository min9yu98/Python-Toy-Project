import tkinter.ttk as ttk
from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "day" for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values) # 사용자가 입력가능함 height는 보여주는 목록갯수
combobox.pack()
combobox.set("card payment") #최초목록의 제목

readonly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly") # 읽기전용
readonly_combobox.current(0) #0번째 인덱스값 선ㅌㅐㄱ
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값을 출력
    print(readonly_combobox.get())

btn = Button(root, text="selection", command=btncmd)
btn.pack()


root.mainloop()