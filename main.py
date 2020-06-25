dis ="""Order Mangement System
    This project is build fully on Python
    You need to login with username: Administrator, password: 12345
    Enjoy
"""
import Singin_page
from tkinter import *
root = Tk()
def goahead():
    root.destroy()
    Singin_page.start()
    exit()
Label(root,text=dis,font=("Arial",12),fg=Singin_page.fg,bg=Singin_page.bg).pack()
Button(root,text="Go Ahead!!",font=("Arial",12),fg=Singin_page.fg,bg='black',command=goahead).pack()
root.title("HEllo There!!")
root.config(bg=Singin_page.bg)
root.geometry("500x250")
root.mainloop()
exit()