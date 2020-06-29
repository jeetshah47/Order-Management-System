from tkinter import *
import tkinter.messagebox as m
import dashboard_py
def main():
    bg = 'maroon'
    count = 0
    window=Tk()
    window.config(bg=bg)
    #menu
    
    #Function for command
    lbl=Label(window, text="Order ID :", fg='lawn green',bg=bg, font=("Helvetica", 10))
    lbl.place(x=10, y=10)
    f1 = open("resources/order_id.txt","r")
    fixid = f1.readlines()
    nextid = int(fixid[-1])+1
    print(nextid)
    #id_get = txtfld.get()
    #f1.write("\n"+id_get)
    f1.close()
    txtfld=Label(window, text=nextid, bd=2, font=("Helvetica", 10),bg=bg,fg="white")
    txtfld.place(x=67, y=10, width=180)
    def check():
        changes = True
        if txtfld1.get() == "" or   C1.get() == ""  or C2.get() == ""  or txtfld6.get() == "" or v0.get() == None:
            m.showerror("NO","Please enter proper details")
            changes =  False
        if changes:
            save_in_file()
    #txtfld.insert(0,"Enter a valid id")
    def save_in_file():
        f1 = open("resources/order_id.txt","a+")
        f1.write("\n"+str(nextid))
        f1.close()
        f2 = open('resources/customer_id.txt','a+')
        customer_id = txtfld1.get()
        f2.write("\n"+customer_id)
        f2.close()
        f3 = open('resources/product.txt','a+')
        products = C1.get()
        f3.write("\n"+products)
        f3.close()
        f4 = open('resources/addresses.txt','a+')
        addresses = C2.get()
        f4.write("\n"+addresses)
        f4.close()
        f5 = open('resources/tc.txt','a+')
        tcs = txtfld6.get()
        f5.write("\n"+tcs)
        f5.close()
        f6 = open('resources/mode.txt','a+')
        modes = v0.get()
        f6.write("\n"+modes)
        f6.close()
    # customer name
    lbl=Label(window, text="Customer Name :", fg='lawn green',bg=bg ,font=("Helvetica", 10))
    lbl.place(x=10, y=40)
    txtfld1=Entry(window, text="random text2", bd=2, font=("Helvetica", 10))
    txtfld1.place(x=150, y=40, width=180)

    # product selection
    lbl=Label(window, text="Products Details :", fg='lawn green',bg=bg, font=("Helvetica", 10))
    lbl.place(x=10, y=80)

    C1 = Entry(window,font=('Helvetica',10),bg='white',fg='black' ,bd=2)
    C1.place(x=150, y=80)
    C1.delete(0,END)
    Label(window,text="Address: ",bg=bg,fg='lawn green',font=('Helvetica',10)).place(x=10,y=120)
    C2 = Entry(window,font=('Helvetica',10),bg='white',fg='black',width=30,bd=2)
    C2.place(x = 150,y = 120)
    # Quantity of products
    # Total cost
    lbl=Label(window, text="Total Cost :", fg='lawn green',bg=bg, font=("Helvetica", 10))
    lbl.place(x=10, y=180)
    txtfld6=Entry(window, text="random text7", bd=2)
    txtfld6.place(x=150, y=180, width=180)

    # Selection of payment mode
    lbl=Label(window, text="Select the payment mode of the order from below :", bg=bg,fg='lawn green', font=("Helvetica", 10))
    lbl.place(x=10, y=210)
    v0=StringVar()
    v0.set(None)
    r1=Radiobutton(window, text="Cash on delivery", bg=bg,variable=v0,fg='pink',value="COD")
    r2=Radiobutton(window, text="Online Payment", bg=bg,fg='pink',variable=v0,value="ONLINE")
    r1.place(x=50,y=230)
    r2.place(x=180, y=230)

    def ask_yes_no():
        ask = m.askyesnocancel("Cancel Order","Are you sure you want to cancel")
        if ask:
            window.destroy()
    def goback():
        window.destroy()
        dashboard_py.main()
        exit()
    # Entering/Cancelling the Order
    btn=Button(window, text="Enter Order", bg='black', fg='white',font=("Helvetica", 10),command = check, bd=2)
    btn.place(x=10, y=260)
    btn=Button(window, text="Cancel Order", bg='black',fg='white', font=("Helvetica", 10), bd=2,command=ask_yes_no)
    btn.place(x=150, y=260)
    btn=Button(window, text="Go back", bg='black', fg='white',font=("Helvetica", 10),command=goback, bd=2)
    btn.place(x=300, y=260)
    window.title('Add Order')
    window.geometry("400x300+100+100")
    window.mainloop()
if __name__ == "__main__":
    main()
