from tkinter import *
import dashboard_py
import tkinter.messagebox as m
import hashlib
bg = 'maroon'
fg = 'white'
def start():
    root = Tk()
    root.config(bg = bg)
    Label(text="Choose Your account Type",bg=bg,fg=fg,font=("Arial",16)).pack()
    def access(event):
        txtpass = user_pass.get()
        hashpass = hashlib.md5(txtpass.encode())
        if user_name.get() == "Administrator" and hashpass.hexdigest() == "827ccb0eea8a706c4c34a16891f84e7b":
            m.showinfo("Access granted","You have succesfully log in as admin")
            root.destroy()
            dashboard_py.main()
            exit()            
        else:
            m.showwarning("No input","Please enter the details")
    Label(root,text="Enter User Name and Password",bg=bg,fg=fg,font=("Arial",12)).place(x=200,y=80)
    Label(root,text="Username: ",font=("Arial",12),bg=bg,fg=fg).place(x=160,y=126)
    Label(root,text="Password: ",font=("Arial",12),bg=bg,fg=fg).place(x=160,y=156)
    user_name = Entry(root)
    user_name.place(x = 250, y = 130)
    user_pass = Entry(root,show="*")
    user_pass.place(x = 250, y = 158)
    Button(root,text="Login",font=("Arial",10),bg='black',fg='white',command=lambda: access("")).place(x=280,y=200)
    root.bind("<Return>",access)
    root.geometry("600x300")
    root.mainloop()
if __name__ == "__main__":
    start()