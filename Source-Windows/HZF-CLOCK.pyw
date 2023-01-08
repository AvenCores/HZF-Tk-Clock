from tkinter import Tk,Label,CENTER,Button
from time import strftime
from datetime import date
import ctypes as ct

root = Tk()
root.title("HZF Clock")
root.configure(bg='#000000')
root.geometry("250x250")
root.resizable(width=False, height=False)

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

poetry = 't.me/hzfnews'
label1 = Label(text=poetry, justify=CENTER, bg="#000000", fg="white", font="Ubuntu 10")
label1.place(x=85, y=5)

root.deiconify()
root.mainloop()