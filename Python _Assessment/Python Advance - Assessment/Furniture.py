from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="furniture_company"
        )

def insert_Data():
    if e_id.get() == "" or e_pName.get() == "" or e_pPrice.get() == "" or e_pQty.get() == "":
        msg.showinfo("Insert Status", "All Fields Are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into furniture_database(id,pName,pPrice,pQty) values (%s, %s, %s, %s)"
        args = (e_id.get(), e_pName.get(), e_pPrice.get(), e_pQty.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        e_id.delete(0, 'end')
        e_pName.delete(0, 'end')
        e_pPrice.delete(0, 'end')
        e_pQty.delete(0, 'end')
        msg.showinfo("Insert Status", "Data Inserted Successfully")

def search_Data():
    e_pName.delete(0, 'end')
    e_pPrice.delete(0, 'end')
    e_pQty.delete(0, 'end')
    if e_id.get() == "":
        msg.showinfo("Search Status", "ID is Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from furniture_database where id=%s"
        args = (e_id.get(),)
        cursor.execute(query, args)
        row = cursor.fetchone()
        if row:
            e_pName.insert(0, row[1])
            e_pPrice.insert(0, row[2])
            e_pQty.insert(0, row[3])
        else:
            msg.showinfo("Search Status", "ID Not Found")
        conn.close()

def delete_Data():

    if e_id.get()=="":
         msg.showinfo("Delete Status","ID Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from furniture_database where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0, 'end')
        e_pName.delete(0, 'end')
        e_pPrice.delete(0, 'end')
        e_pQty.delete(0, 'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")


def update_Data():
    if e_id.get() == "" or e_pName.get() == "" or e_pPrice.get() == "" or e_pQty.get() == "":
        msg.showinfo("Update Status", "All Fields Are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "UPDATE furniture_database SET pName=%s, pPrice=%s, pQty=%s WHERE id=%s"
        args = (e_pName.get(), e_pPrice.get(), e_pQty.get(), e_id.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        e_id.delete(0, 'end')
        e_pName.delete(0, 'end')
        e_pPrice.delete(0, 'end')
        e_pQty.delete(0, 'end')
        msg.showinfo("Update Status", "Data Updated Successfully")

def total_Price():
    if e_id.get()=="" or e_pName.get()=="" or e_pPrice.get()=="" or e_pQty.get()=="":
        msg.showinfo("Total Price","All Fields Are Mandatory")

    else:
        conn = create_conn()
        cursor = conn.cursor()
        
        price= float(e_pPrice.get())
        quantity=int(e_pQty.get())

        total = price * quantity

        l_total.config(text=f"Total price : {total:.2f}")



root = Tk()
root.geometry("750x550")
root.title("My Furniture App")
root.resizable(width=False, height=False)

# Labels
header = Label(root, text="Stock Calculator", font=("Arial", 25,"bold"))
header.place(x=230, y=5)

Items = Label(root, text="List of items", font=("Arial", 15,"bold"))
Items.place(x=560, y=60)

chair = Label(root, text="111 - Chair", font=("Arial", 13))
chair.place(x=570, y=100)

table = Label(root, text="222 - Table", font=("Arial", 13))
table.place(x=570, y=130)

table = Label(root, text="333 - Cupboard", font=("Arial", 13))
table.place(x=570, y=160)

Sofa = Label(root, text="444 - Sofa", font=("Arial", 13))
Sofa.place(x=570, y=190)

Bed = Label(root, text="555 - Bed", font=("Arial", 13))
Bed.place(x=570, y=220)

Dresser = Label(root, text="666 - Dresser", font=("Arial", 13))
Dresser.place(x=570, y=250)

Bookcase = Label(root, text="777 - Bookcase", font=("Arial", 13))
Bookcase.place(x=570, y=280)

TV_stand = Label(root, text="888 - TV stand", font=("Arial", 13))
TV_stand.place(x=570, y=310)


l_id = Label(root, text="ID", font=("Arial", 15,"bold"))
l_id.place(x=50, y=80)

l_pName = Label(root, text="Product Name", font=("Arial", 15,"bold"))
l_pName.place(x=50, y=130)

l_pPrice = Label(root, text="Product Price", font=("Arial", 15,"bold"))
l_pPrice.place(x=80, y=210)

l_cross = Label(root, text="X", font=("Arial", 15,"bold"))
l_cross.place(x=260, y=230)

l_pQty = Label(root, text="Product Quantity", font=("Arial", 15,"bold"))
l_pQty.place(x=320, y=210)

l_total = Label(root, text="", font=("Arial", 15,"bold"))
l_total.place(x=170, y=350)


# Entry
e_id = Entry(root, width=25, font=("Arial", 15))
e_id.place(x=220, y=80)

e_pName = Entry(root, width=25, font=("Arial", 15))
e_pName.place(x=220, y=130)

e_pPrice = Entry(root, width=10, font=("Arial", 15))
e_pPrice.place(x=90, y=250)

e_pQty = Entry(root, width=10, font=("Arial", 15))
e_pQty.place(x=340, y=250)


# Buttons

insert = Button(root, text="Insert", bg="darkblue", fg="white",width=7, font=("Arial", 14,"bold"), command = insert_Data)
insert.place(x=80, y=450)

search = Button(root, text="Search", bg="darkblue", fg="white",width=7, font=("Arial", 14,"bold"), command = search_Data)
search.place(x=195, y=450)

delete = Button(root, text="Delete", bg="darkblue", fg="white",width=7,font=("Arial", 14,"bold"),command = delete_Data)
delete.place(x=310, y=450)

update = Button(root, text="Update", bg="darkblue", fg="white",width=7,font=("Arial", 14,"bold"), command = update_Data)
update.place(x=425, y=450)

total = Button(root, text="Total", bg="darkblue", fg="white",width=7,font=("Arial", 14,"bold"),command = total_Price)
total.place(x=540, y=450)

root.mainloop()
