from tkinter import *
import tkinter.messagebox as m
import Singin_page
import dashboard_py
#Color Scheme for Label
bg = 'maroon'
fg = 'white'
start = 0
def main():
    #File management
    root1 = Tk()
    root1.config(bg=bg)
    #Module Function
    def Sinin_page():
        root1.withdraw()
        Singin_page.start()
    menubar = Menu(root1)
    def goback():
        root1.destroy()
        dashboard_py.main()
        exit()
    
    #Back Button
    Button(root1,text="Go back",font=('Arial'),command=goback,bg='black',fg='white').place(x=360,y=20)
    
    #Order System
    def dynamic(event):
        s_id = StringVar()
        s_id.set(order_id.get())
        order_id.delete(0,END)
        l=Label(root1,text="Click on clear to search more orders",font=("Arial",12),bg=bg,fg=fg)
        l.place(x=100,y=250)
        search_frame = Frame(root1)
        search_frame.place(x = 70,y = 70)
        search_frame.config(bg="white")
        def clear():
            search_frame.destroy()
            l.destroy()
        clear_btn=Button(root1,text="Clear Result",font=('Arial'),command=clear,bg='black',fg='white').place(x=449,y=20)
        id = str(s_id.get())
        f1 = open('resources/order_id.txt','r')
        order_ids = f1.readlines()
        f1.close()
        f2 = open('resources/customer_id.txt','r')
        customer_id  = f2.readlines()
        f2.close()
        f3 = open('resources/product.txt','r')
        products = f3.readlines()
        f3.close()
        f4 = open('resources/addresses.txt','r')
        addresses = f4.readlines()
        f4.close()
        f5 = open('resources/mode.txt','r')
        modes = f5.readlines()
        f5.close()
        f6 = open('resources/tc.txt','r')
        tcs = f6.readlines()
        f6.close()
        address = None
        if id == "":
            m.showerror("Wrong Id","You have entered Wrong id")
        else:
            flag = 0
            for i in range(len(order_ids)):
                if id in order_ids[i]:
                    address_name = addresses[i]
                    product = products[i]
                    name = customer_id[i]
                    mode = modes[i]
                    tc = tcs[i]
                    Label(search_frame,text="You searched for "+id,bg='white',font=('Arial',8)).grid(row=0,column=0,sticky=W)
                    Label(search_frame,text="Order Details",bg='white',font=("sans-serif",20)).grid(row=1,column=0,pady=10,sticky=W)
                    Label(search_frame,text="Ordered On 9th month",bg='white',font=("sans-serif",14)).grid(row=2,column = 0,pady = 5,sticky=W)
                    Label(search_frame,text="Customer name",bg='white',font=("sans-serif",14)).grid(row=3,column = 0,sticky=W)
                    Label(search_frame,text="Product name",bg='white',font=("sans-serif",14)).grid(row=3,column = 1,sticky=W)
                    Label(search_frame,text="Shipping Address",bg='white',font=("sans-serif",14)).grid(row=3,column = 2,sticky=W,padx=3)
                    Label(search_frame,text="Payment Mode",bg='white',font=("sans-serif",14)).grid(row=3,column=3,sticky=W,padx=3)
                    Label(search_frame,text="Total Cost",bg='white',font=("sans-serif",14)).grid(row=3,column=4,sticky=W,padx=3)
                    Label(search_frame,text=name,bg='white',font=("sans-serif",12)).grid(row=4,column=0)
                    Label(search_frame,text=product,bg='white',font=("sans-serif",12)).grid(row=4,column=1)
                    Label(search_frame,text=address_name,bg='white',font=("sans-serif",12)).grid(row=4,column=2)
                    Label(search_frame,text=mode,bg='white',font=("sans-serif",12)).grid(row=4,column=3)
                    Label(search_frame,text=tc,bg='white',font=("sans-serif",12)).grid(row=4,column=4)
                   # print(line[i][6:])
                    flag = 1
            if flag == 0:
                m.showerror("Alert","Given Id was not founded in our database")
        print(id)
    Label(root1,text="Order ID: ",font=("Arial",12),bg=bg,fg=fg).pack(side=LEFT,ipadx = 30,ipady=20,anchor=N)
    order_id = Entry(root1)
    order_id.place(x=100,y=22)
    submit_btn=Button(text="Search",font=("Arial"),command=lambda: dynamic(""),bg='black',fg='white').place(x=280,y = 20)
    root1.bind("<Return>",dynamic)
    #File menus
  
    root1.geometry("1000x450")
    root1.mainloop()

if __name__ == "__main__":
    main()
