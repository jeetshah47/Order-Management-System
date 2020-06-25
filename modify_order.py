from tkinter import *
import tkinter.messagebox as m
import dashboard_py
#Color Scheme for Label
bg = 'maroon'
fg = 'lawn green'
def main():
    window=Tk()
    #modify with order id
    lbl=Label(window, text="Enter the order ID to modify below :", fg=fg,bg=bg, font=("Helvetica", 10))
    lbl.place(x=95, y=10)
    txtfld=Entry(window, text="random text1", bd=2)
    txtfld.place(x=120, y=30, width=160)
    def goback():
        window.destroy()
        dashboard_py.main()
        exit()
    #Back Button
    #File Management
    def modify_save():
        f1 = open('resources/order_id.txt','r')
        ids = f1.readlines()
        id = txtfld.get()
       # print(ids)
        f2 = open('resources/customer_id.txt','r')
        flag = 0
        index = 0
        custom = f2.readlines()
        f2.close()
        f2 = open('resources/customer_id.txt','w')
        f3 = open('resources/product.txt','r')
        products = f3.readlines()
        f3.close()
        f3 = open('resources/product.txt','w')
        f4 = open('resources/addresses.txt','r')
        addresses = f4.readlines()
        f4.close()
        f4 = open('resources/addresses.txt','w')
        f5 = open('resources/tc.txt','r')
        tcs = f5.readlines()
        f5.close()
        f5 = open('resources/tc.txt','w')
        f6 = open('resources/mode.txt','r')
        modes = f6.readlines()
        f6.close()
        f6 = open('resources/mode.txt','w')
        for i in range(len(ids)):
            if id in ids[i]:
                flag = 1
                index = i
                print(custom)
        if flag:
            print(custom[index])
            if index < len(custom)-1:
                temp1 = txtfld1.get() + '\n'
                temp2 = C1.get() + '\n'
                temp3 = C2.get() 
                print(C2.get())
                temp4 = txtfld6.get() + '\n'
                print(txtfld6.get())
                temp5 = v0.get() + '\n'
                print(temp5)
                custom[index] = temp1
                products[index] = temp2
                addresses[index] = temp3
                tcs[index] = temp4
                modes[index] = temp5
            else:
                custom[index] = txtfld1.get()
                products[index] = C1.get()
                addresses[index] = C2.get()
                tcs[index] = txtfld6.get()
                modes[index] = v0.get()
            
            c = ""
            p = ""
            a = ""
            t = ""
            m = ""
            for i in custom:
                c += i
            f2.write(c)
            for i in products:
                p += i
            f3.write(p)
            for i in addresses:
                a += i
            print(a)
            f4.write(a)

            for i in tcs:
                t += i
            print(t)
            f5.write(t)
            for i in modes:
                m += i
            print(m)
            f6.write(m)
        else:
            print("Not Found")
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
    #Customer name
    lbl=Label(window, text="Add the required modifications below :",  font=("Helvetica", 10), fg=fg,bg=bg)
    lbl.place(x=10, y=60)
    lbl=Label(window, text="Customer Name :", font=("Helvetica", 10), fg=fg,bg=bg)
    lbl.place(x=10, y=90)
    txtfld1=Entry(window, text="random text2", bd=2)
    txtfld1.place(x=150, y=90, width=180)

    #Product selection
    lbl=Label(window, text="Products Details :", fg='lawn green',bg=bg, font=("Helvetica", 10))
    lbl.place(x=10, y=120)

    C1 = Entry(window,font=('Helvetica',10),bg='white',fg='black' ,bd=2)

    C1.place(x=150, y=120)
    C1.delete(0,END)
    C1.insert(0,"Enter Product Name")

    Label(window,text="Address: ",bg=bg,fg='lawn green',font=('Helvetica',10)).place(x=10,y=150)
    C2 = Entry(window,font=('Helvetica',10),bg='white',fg='black',width=30,bd=2)
    C2.insert(0,"Enter address")
    C2.place(x = 150,y = 150)
    #Product quantity

    #Total Cost
    lbl=Label(window, text="Total Cost :",  font=("Helvetica", 10), fg=fg,bg=bg)
    lbl.place(x=10, y=210)
    txtfld6=Entry(window, text="random text7", bd=2)
    txtfld6.place(x=150, y=210, width=180)

    #Payment mode
    lbl=Label(window, text="Modify payment mode of the order below :",fg=fg,bg=bg ,font=("Helvetica", 10))
    lbl.place(x=10, y=240)
    v0=StringVar()
    v0.set(None)
    r1=Radiobutton(window, text="Cash on delivery", variable=v0,value="COD", fg='yellow',bg=bg)
    r2=Radiobutton(window, text="Online Payment", variable=v0,value="ONLINE", fg='yellow',bg=bg)
    r1.place(x=50,y=260)
    r2.place(x=180, y=260)

    #Entering/Cancelling changes
    #Function to ask yes,no
    def ask_yes_no():
        ask= m.askokcancel("Cancel Modification","Are you sure you want to cancel modification")
        if ask:
            window.destroy()
    btn=Button(window, text="Modify Order", fg='black', font=("Helvetica", 10), bd=2,command=modify_save)
    btn.place(x=10, y=300)
    btn=Button(window, text="Cancel Changes", fg='black', font=("Helvetica", 10),command=ask_yes_no, bd=2)
    btn.place(x=150, y=300)
    btn=Button(window, text="Go Back", fg='black', font=("Helvetica", 10),command=goback, bd=2)
    btn.place(x=300, y=300)

    window.title('Modify Orders')
    window.config(bg=bg)
    window.geometry("400x350+100+100")
    window.mainloop()
if __name__ == "__main__":
    main()
