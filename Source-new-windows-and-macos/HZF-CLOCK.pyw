from tkinter import Label, CENTER, Menu
from tkinter import messagebox
from time import strftime
from datetime import date
import customtkinter
import webbrowser
import darkdetect
import tkinter

#######
version = "3.5"
autor = "avencores"
libs = "Tkinter | CustomTkinter"
about = "HZF Tk Clock - это простые часы на базе графического интерфейса Tk и модификации CustomTkinter."
#######

customtkinter.set_appearance_mode("system") # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green

root = customtkinter.CTk() # Создает окно
root.geometry("292x250") # Размеры окна
root.title("HZF Clock") # Название окна
root.resizable(width=False, height=False) # Запрет на модификацию окна по высоте и ширине
root.iconbitmap("ICO/clock.ico") # Иконка приложения

# Dark and Light
if darkdetect.theme() == "Dark":
        def timenow():
                current_time = strftime("%H : %M : %S")
                clock.config(text=current_time)
                clock.after(200,timenow)

        clock=Label(root, justify=CENTER, bg="#242424", fg="#ffffff", font=("ubuntu",30,"bold"))
        clock.grid(row=2,column=2,pady=60,padx=45)
        timenow()

        godate = date.today()
        current_date = godate.strftime("%d.%m.%y")
        datenow2=Label(text=current_date, font="ubuntu", bg="#242424", fg="#ffffff", justify=CENTER)
        datenow2.place(x=110, y=120)

elif darkdetect.theme() == "Light": 
        def timenow():
                current_time = strftime("%H : %M : %S")
                clock.config(text=current_time)
                clock.after(200,timenow)

        clock=Label(root, justify=CENTER, bg="#EBEBEB", fg="#000000", font=("ubuntu",30,"bold"))
        clock.grid(row=2,column=2,pady=60,padx=45)
        timenow()

        godate = date.today()
        current_date = godate.strftime("%d.%m.%y")
        datenow2=Label(text=current_date, bg="#EBEBEB", fg="#000000",font="ubuntu", justify=CENTER)
        datenow2.place(x=110, y=120)


def godapptk():
    root.attributes("-topmost",True) # Закрепить

def notgodapptk():
    root.attributes("-topmost",False) # Открепить

button = customtkinter.CTkButton(master=root, fg_color="#00FF00", hover_color="#32CD32", text_color="black", text="Закрепить часы", command=godapptk)
button.place(x=150, y=180, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=root, fg_color="red", hover_color="#8B0000", text_color="white", text="Открепить часы", command=notgodapptk)
button.place(x=150, y=220, anchor=tkinter.CENTER)

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
        windowsadd = customtkinter.CTk()
        windowsadd.geometry("300x100")
        windowsadd.title("Сбер Донат")
        windowsadd.resizable(width=False, height=False)
        windowsadd.iconbitmap("ICO/clock.ico")
        label = customtkinter.CTkLabel(master=windowsadd, font=("ubuntu",20,"bold"), text="2202 2050 7215 4401")
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        windowsadd.mainloop()


def vtb():
        windowsadd = customtkinter.CTk()
        windowsadd.geometry("300x100")
        windowsadd.title("ВТБ Донат")
        windowsadd.resizable(width=False, height=False)
        windowsadd.iconbitmap("ICO/clock.ico")
        label = customtkinter.CTkLabel(master=windowsadd, font=("ubuntu",20,"bold"), text="2200 2404 1001 8580")
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        windowsadd.mainloop()

def omyprog():
        messagebox.showinfo(title="О программе", message=f"""{about}

Автор утилиты: {autor}

Интерфейс: {libs}

Версия: {version}
    """)

def infogui():
        window = customtkinter.CTk()
        window.geometry("200x200")
        window.title("")
        window.resizable(width=False, height=False)
        window.iconbitmap("ICO/clock.ico")
        button = customtkinter.CTkButton(master=window, text="Telegram Channel", command=opentgchannel)
        button.place(x=30, y=25)
        button = customtkinter.CTkButton(master=window, text="YouTube Channel", command=openytchannel)
        button.place(x=30, y=65)
        button = customtkinter.CTkButton(master=window, text="Discord Channel", command=opendiscord)
        button.place(x=30, y=105)
        button = customtkinter.CTkButton(master=window, text="VK Group", command=openvkgroup)
        button.place(x=30, y=145)
        window.mainloop()
        window.quit()

def donategui():
        window = customtkinter.CTk()
        window.geometry("200x160")
        window.title("")
        window.resizable(width=False, height=False)
        window.iconbitmap("ICO/clock.ico")
        button = customtkinter.CTkButton(master=window, text="Qiwi Донат", command=qiwi)
        button.place(x=30, y=25)
        button = customtkinter.CTkButton(master=window, text="Сбер Донат", command=cber)
        button.place(x=30, y=65)
        button = customtkinter.CTkButton(master=window, text="ВТБ Донат", command=vtb)
        button.place(x=30, y=105)
        window.mainloop()

def spravka():
        window = customtkinter.CTk()
        window.geometry("200x120")
        window.title("")
        window.resizable(width=False, height=False)
        window.iconbitmap("ICO/clock.ico")
        button = customtkinter.CTkButton(master=window, text="Написать разработчику", command=devtgopen)
        button.place(x=20, y=25)
        button = customtkinter.CTkButton(master=window, width=159, text="О программе", command=omyprog)
        button.place(x=20, y=65)
        window.mainloop()

button = customtkinter.CTkButton(master=root, width=92, height=25, text="Информация", command=infogui)
button.place(x=0)

button = customtkinter.CTkButton(master=root, width=92, height=25, text="Донат", command=donategui)
button.place(x=100)

button = customtkinter.CTkButton(master=root, width=92, height=25, text="Справка", command=spravka)
button.place(x=200)

root.mainloop()