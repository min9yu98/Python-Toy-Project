from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height = 0) # extended:여러개 선택 , single:한개선택, height = 0이면 다보여주고 height = 1이면 한개만 보여줌

listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # listbox.delete(0) #맨뒤에것 삭제 

    # 개수 확인
    # print("list", listbox.size(), "count")

    # 항목 확인 (시작 인덱스, 끝 인덱스)
    # print("1~3 num : ", listbox.get(0, 2))

    # 선택된 항목 확인(위치반환 - 인덱스 출력)
    print("selected part : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()