from tkinter import *
import time
import datetime
import sys

root = Tk()
root.title("HZF Clock")
root.geometry("250x250")
root.resizable(width=False, height=False)

def timenow():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,timenow)

def datenow():
    date = '2022.09.03'
    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    datenow2.config(text=current_date)
    print(current_date.day)        
    print(current_date.month)      
    print(current_date.year)

clock=Label(root,font=("ubuntu",30,"bold"))
clock.grid(row=2,column=2,pady=60,padx=30)
timenow()

now = datetime.datetime.now()
poetry = (now.year,root,now.month,root,now.day)
datenow2=Label(text=poetry, font="ubuntu", justify=CENTER)
datenow2.place(x=90, y=120)

root.mainloop()