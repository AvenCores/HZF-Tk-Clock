from tkinter import Tk,Label,CENTER,Button,Menu,messagebox
from time import strftime
from datetime import date
from sys import platform
import ctypes as ct
import webbrowser
from requests import get
from os import system

version = "2.8"

if platform == "win32":
    f=open(r'app.ico', "wb")
    ufr = get("https://raw.githubusercontent.com/AvenCores/HZF-Tk-Clock/main/Source/ICO/clock.ico")
    f.write(ufr.content)
    f.close()

    root = Tk()
    root.title("HZF Clock")
    root.configure(bg='#000000')
    root.geometry("250x250")
    root.resizable(width=False, height=False)
    root.iconbitmap("app.ico")

    root.iconify()
    root.update()
    DWWMA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(root.winfo_id())
    renduring_policy = DWWMA_USE_IMMERSIVE_DARK_MODE
    value = 1
    value = ct.c_int(value)
    set_window_attribute(hwnd, renduring_policy, ct.byref(value), ct.sizeof(value))
    root.update_idletasks()

    def timenow():
        current_time = strftime("%H : %M : %S")
        clock.config(text=current_time)
        clock.after(200,timenow)

    clock=Label(root, justify=CENTER, bg="#000000", fg="white", font=("ubuntu",30,"bold"))
    clock.grid(row=2,column=2,pady=60,padx=30)
    timenow()

    godate = date.today()
    current_date = godate.strftime("%d.%m.%y")
    datenow2=Label(text=current_date, bg="#000000", fg="white", font="ubuntu", justify=CENTER)
    datenow2.place(x=90, y=120)

    def godapptk():
        root.attributes("-topmost",True)

    def notgodapptk():
        root.attributes("-topmost",False)

    file = Button(text='Закрепить часы', bg="green", fg="white", command=godapptk)
    file.place(x=75, y=180)

    file = Button(text='Открепить часы', bg="red", fg="white", command=notgodapptk)
    file.place(x=75, y=210)

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

Интерфейс: Tkinter

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

    root.deiconify()
    root.mainloop()
    system("del /Q app.ico")

elif platform == "linux" or platform == "linux2" or platform == "unix":
    f=open(r'app.ico', "wb")
    ufr = get("https://raw.githubusercontent.com/AvenCores/HZF-Tk-Clock/main/Source/ICO/clock.ico")
    f.write(ufr.content)
    f.close()

    root = Tk()
    root.title("HZF Clock")
    root.geometry("250x250")
    root.resizable(width=False, height=False)
    root.iconbitmap("app.ico")

    def timenow():
        current_time = strftime("%H : %M : %S")
        clock.config(text=current_time)
        clock.after(200,timenow)

    clock=Label(root,justify=CENTER,font=("ubuntu",30,"bold"))
    clock.grid(row=2,column=2,pady=60,padx=30)
    timenow()

    godate = date.today()
    current_date = godate.strftime("%d.%m.%y")
    datenow2=Label(text=current_date, font="ubuntu", justify=CENTER)
    datenow2.place(x=90, y=120)

    def godapptk():
        root.attributes("-topmost",True)

    def notgodapptk():
        root.attributes("-topmost",False)

    file = Button(text='Закрепить часы', bg="green", fg="white", command=godapptk)
    file.place(x=75, y=180)

    file = Button(text='Открепить часы', bg="red", fg="white", command=notgodapptk)
    file.place(x=75, y=210)

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

Интерфейс: Tkinter

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