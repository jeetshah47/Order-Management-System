from tkinter import *
import dashboard_py
import tkinter.messagebox as m
#Color Scheme for Label
bg = 'maroon'
fg = 'white'
#Initial Design 1.0
def main():
    root = Tk()
    root.config(bg=bg)
    Label(root,text= "All ORDERS ARE GIVEN BELOW",font=('sans-serif',16),bg=bg,fg='pale green').pack(pady=30)
    def goback():
        root.destroy()
        dashboard_py.main()
        exit()
    table_frame = Frame(root,bg=bg,width=900,height=500)
    Button(root,text = "Go Back",command=goback,bg='black',fg='white').place(x=35,y =30)
    def table():
        header = ["Order Id","Customer Name","Product","Address","Payment Mode","Total Cost"]
        f1 = open('resources/order_id.txt','r')
        order_ids = f1.readlines()
        print(order_ids)
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
        table_head = Frame(table_frame,bg=bg)
        table_head.place(x=0,y=0)
        head_iterator = iter(header)
        a = 0
        while head_iterator:
            try:
                head = next(head_iterator)
                Label(table_head,text=head,font=('Arial',12),bg=bg,fg='yellow').grid(row=0,column=a)
                a += 1
            except StopIteration:
                break

        #for i in range(len(header)):
            #Label(table_head,text=header[i],font=('Arial',12),bg=bg,fg='yellow').grid(row=0,column=i)

        for i in range(len(order_ids)):
            print(order_ids[i])
            Label(table_head,text=order_ids[i],font=('Arial',12),bg=bg,fg=fg).grid(row=i+1,column=0,sticky=W)
            Label(table_head,text=customer_id[i],font=('Arial',12),bg=bg,fg=fg).grid(row=i+1,column=1,sticky=W)
            Label(table_head,text=products[i],font=('Arial',12),bg=bg,fg=fg).grid(row=i+1,column=2,sticky=W) 
            Label(table_head,text=addresses[i],font=('Arial',12),bg=bg,fg=fg).grid(row=i+1,column=3,sticky=W)
            Label(table_head,text=modes[i],font=('Arial',12),bg=bg,fg=fg).grid(row=i+1,column=4,sticky=W,padx=15)
            Label(table_head,text=tcs[i],font=('Arial',12),bg=bg,fg=fg).grid(row=i+1,column=5,sticky=W)
    table()
    table_frame.place(x = 25, y = 70)
    root.geometry('900x500')
    root.mainloop()
if __name__ == "__main__":
    main()
