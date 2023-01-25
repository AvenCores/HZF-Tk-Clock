import customtkinter
from tkinter import Label, CENTER, Menu
import tkinter
from tkinter import messagebox
from time import strftime
from datetime import date
import webbrowser

version = "2.9"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("250x250")
root.title("HZF Clock")
root.resizable(width=False, height=False)

def timenow():
    current_time = strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,timenow)

clock=Label(root, justify=CENTER, bg="#242424", fg="#ffffff", font=("ubuntu",30,"bold"))
clock.grid(row=2,column=2,pady=40,padx=30)
timenow()

godate = date.today()
current_date = godate.strftime("%d.%m.%y")
datenow2=Label(text=current_date, font="ubuntu", bg="#242424", fg="#ffffff", justify=CENTER)
datenow2.place(x=90, y=100)

def godapptk():
    root.attributes("-topmost",True)

def notgodapptk():
    root.attributes("-topmost",False)

button = customtkinter.CTkButton(master=root, text="Закрепить часы", command=godapptk)
button.place(x=125, y=160, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=root, text="Открепить часы", command=notgodapptk)
button.place(x=125, y=200, anchor=tkinter.CENTER)

def opentgchannel():
        url = "https://t.me/hzfnews"
        webbrowser.open(url, new=2)

def openytchannel():
        url = "https://www.youtube.com/c/HZFYT"
        webbrowser.open(url, new=2)

def opendiscord():
        url = "https://discord.com/invite/7bneGfUS5h"
        webbrowser.open(url, new=2)

def openvkgroup():
        url = "https://vk.com/hzforum1"
        webbrowser.open(url, new=2)

def devtgopen():
        url = "https://t.me/avencores"
        webbrowser.open(url, new=2)

def qiwi():
        url = "http://qiwi.com/n/AVENCORESDONATE"
        webbrowser.open(url, new=2)

def cber():
        messagebox.showinfo(title="Сбер Донат", message="2202 2050 7215 4401")

def vtb():
        messagebox.showinfo(title="ВТБ Донат", message="2200 2404 1001 8580")

def omyprog():
        messagebox.showinfo(title="О программе", message=f"""HZF Tk Clock - это простые часы на базе графического интерфейса Tk.

Автор утилиты: avencores

Интерфейс: Tkinter | customtkinter

Версия: {version}
    """)

mainmenu = Menu(root) 
root.config(menu=mainmenu)

mygroup = Menu(mainmenu, tearoff=0)
mygroup.add_command(label="Telegram Channel", command=opentgchannel)
mygroup.add_command(label="YouTube Channel", command=openytchannel)
mygroup.add_command(label="Discord Channel", command=opendiscord)
mygroup.add_command(label="VK Group", command=openvkgroup)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Написать разработчику", command=devtgopen)
helpmenu.add_separator()  
helpmenu.add_command(label="О программе", command=omyprog)

donatemenu = Menu(mainmenu, tearoff=0)
donatemenu.add_command(label="Qiwi Донат", command=qiwi)
donatemenu.add_command(label="Сбер Донат", command=cber)
donatemenu.add_command(label="ВТБ Донат", command=vtb)

mainmenu.add_cascade(label="Информация", menu=mygroup)
mainmenu.add_cascade(label="Донат", menu=donatemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

root.mainloop()