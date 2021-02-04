import time
import tkinter.ttk as ttk
from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# progressbar.start(10) # 10미리세컨드마다 움직임
# progressbar.pack()

# def btncmd():
#    progressbar.stop() # 작동중지



# btn = Button(root, text="pause", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기
        
        p_var2.set(i) # progressbar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="start", command=btncmd2)
btn.pack()
root.mainloop()