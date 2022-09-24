from tkinter import Tk,Label,CENTER
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

clock=Label(root,justify=CENTER,font=("ubuntu",30,"bold"))
clock.grid(row=2,column=2,pady=60,padx=30)
timenow()

godate = date.today()
current_date = godate.strftime("%Y.%m.%d")
datenow2=Label(text=current_date, font="ubuntu", justify=CENTER)
datenow2.place(x=90, y=120)

root.mainloop()