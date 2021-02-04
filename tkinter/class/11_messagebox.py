import tkinter.messagebox as msgbox
from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템이라 가정
def info():
    msgbox.showinfo("notice", "nomally order now")

def warn():
    msgbox.showwarning("warning", "sold out")

def error():
    msgbox.showerror("error", "payment error")

def okcancel():
    msgbox.askokcancel("verification canceling", "this place error, do you want to order")

def retrycancel():
    response = msgbox.askretrycancel("retry / cancel", "temporary error!! would you try again?")
    print("response", response)
    if response == 1:
        print("retry")
    elif response == 0:
        print("cancel")

def yesno():
    msgbox.askyesno("yes / no", "this seat is reverse")

def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = "ticketing is not saved, would you terminate the program after saving?")
    # 네: 저장후 종료
    # 아니요: 저장하지 않고 종료
    # 취소: 프로그램 종료 취소(현재화면에서 계속 작업)
    print("response: ", response) # True or False, None -> 예 1, 아니요 2, 그외
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")

Button(root, command=info, text="notice").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=error, text="error").pack()

Button(root, command=okcancel, text="verification canceling").pack()
Button(root, command=retrycancel, text="retry canceling").pack()
Button(root, command=yesno, text="yes or no").pack()
Button(root, command=yesnocancel, text="yes or no or cancel").pack()


root.mainloop()