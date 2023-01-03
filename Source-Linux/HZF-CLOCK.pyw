from tkinter import Tk,Label,CENTER,Button
from time import strftime
from datetime import date

root = Tk()
root.title("HZF Clock")
root.geometry("250x250")
root.resizable(width=False, height=False)

def timenow():
    current_time = strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,timenow)

clock=Label(root,justify=CENTER,font=("ubuntu",20,"bold"))
clock.grid(row=2,column=2,pady=60,padx=30)
timenow()

godate = date.today()
current_date = godate.strftime("%d.%m.%y")
datenow2=Label(text=current_date, font="ubuntu", justify=CENTER)
datenow2.place(x=87, y=120)

def godapptk():
    root.attributes("-topmost",True)

def notgodapptk():
    root.attributes("-topmost",False)

file = Button(text='Закрепить часы', command=godapptk)
file.place(x=65, y=180)

file = Button(text='Открепить часы', command=notgodapptk)
file.place(x=65, y=210)

poetry = 't.me/hzfnews'
label1 = Label(text=poetry, justify=CENTER, font="Ubuntu 10")
label1.place(x=85, y=5)

root.mainloop()