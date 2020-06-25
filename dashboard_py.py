from tkinter import *
import tkinter.messagebox as m
import Singin_page
import order_details1
import add_module1
import modify_order
import display as d
#Storing All path in Variables(String Formatted)

#Color Scheme for Label
bg = 'maroon'
fg = 'white'
def main():
    window=Tk()
    window.config(bg = bg)
    #Successful login
    lbl=Label(window, text="You have successfully logged in !", fg=fg,bg=bg ,font=("Helvetica", 10))
    lbl.place(x=10, y=10)

    #admin profile and image
    lbl=Label(window, text="Admin Profile", font=("Helvetica", 12),fg=fg,bg=bg)
    lbl.place(x=18, y=50)
    photo = PhotoImage(file = "resources/profile4.png", width=130, height=150) 
    Button(window, image = photo,fg='white',bg='black').place(x=10, y=80, width=120, height=140)

    #Dashboard elements
    lbl=Label(window, text="Welcome to the Dashboard", font=("Helvetica", 13), fg=fg,bg=bg)
    lbl.place(x=190, y=50)
    lbl=Label(window, text="Please select from the menu below...", font=("Helvetica", 10), fg=fg,bg=bg)
    lbl.place(x=190, y=70)

    #admin details
    lbl=Label(window, text="Admin Username: Administrator", font=("Helvetica", 10), fg=fg,bg=bg)
    lbl.place(x=13, y=220)
    lbl=Label(window, text="Admin ID", font=("Helvetica", 10), fg=fg,bg=bg)
    lbl.place(x=13, y=240)
    #Logout Action
    def logout():
        ask = m.askyesno("Logout","Are you Sure you want to logout")
        if ask:
            window.destroy()
            Singin_page.start()
            exit()
    btn=Button(window, text="Logout", font=("Helvetica", 10), bd=2,command=logout,fg='white',bg='black')
    btn.place(x=13, y=270)

    #module menu
    #Intent Function
    #Here the decorators have been used
    def destroy():
        window.destroy()
    def display():
        destroy()
        d.main()
        exit()
    def add():
        destroy()
        add_module1.main()
        exit()
    def modify():
        destroy()
        modify_order.main()
        exit()
    def order_details():
        destroy()
        order_details1.main()
        exit()
    def page(modules):
        modules()
#here generators have been used
    def btn_names():
        yield("View All Orders")
        yield("Add New Orders")
        yield("Modify Orders")
        yield("Order Details")
    def buttons():
        btns = btn_names()
        r1=Button(window, text=next(btns), command = lambda: page(display),fg='white',bg='black',width=13)
        r2=Button(window, text=next(btns), command = lambda: page(add),fg='white',bg='black',width=13)
        r3=Button(window, text=next(btns), command = lambda: page(modify),fg='white',bg='black',width=13)
        r4=Button(window, text=next(btns), command = lambda: page(order_details),fg='white',bg='black',width=13)
        r1.place(x=180,y=100)
        r2.place(x=320, y=100)
        r3.place(x=180, y=150)
        r4.place(x=320, y=150)
    buttons()
    window.title('Dashboard')
    window.geometry("600x320+100+100")
    window.mainloop()
if __name__ == "__main__":
    main()
