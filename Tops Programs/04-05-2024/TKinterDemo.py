# TKinter Demo

from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_python_database"
        )
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" :
        msg.showinfo("Insert Status","All Fiels Are Mandatory")
    else :
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into student(fName,lName,email,mobile) value (%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")     
        msg.showinfo("Insert Status","Data Inserted")

def search_data():
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")     
        
    
    if e_id.get()=="" :
        msg.showinfo("Search Status","ID is Mandatory")
    else :
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from student where id = %s"
        args = (e_id.get(),)
        cursor.execute(query,args)
       
        row = cursor.fetchall()
        if row :
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
        else :
            msg.showinfo("Search Status","ID Is Not Found")
        conn.close()

def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else :
        conn = create_conn()
        cursor = conn.cursor()
        query = "update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_id.delete(0,"end")
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")     
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory")
    else :
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from student where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_id.delete(0,"end")
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")     
        msg.showinfo("Delete Status","Data Deleted Successfully")




root = Tk()
root.geometry("400x400")
root.title("Registration Form - From Tkinter Example")
root.resizable(width=False,height = False)

l_id = Label(root,text = "ID")
l_id.place(x=50,y=50)

l_fname = Label(root,text = "First name")
l_fname.place(x=50,y=100)

l_lname = Label(root,text = "Last Name")
l_lname.place(x=50,y=150)

l_email = Label(root,text = "Email")
l_email.place(x=50,y=200)

l_mobile = Label(root,text = "Mobile Number")
l_mobile.place(x=50,y=250)

# User Input

e_id = Entry(root)
e_id.place(x=200,y=50)

e_fname = Entry(root)
e_fname.place(x=200,y=100)

e_lname = Entry(root)
e_lname.place(x=200,y=150)

e_email = Entry(root)
e_email.place(x=200,y=200)

e_mobile = Entry(root)
e_mobile.place(x=200,y=250)

# Button

Insert = Button(root,text = "INSERT",bg = "black",fg = "white",font = ("Arial",12), command = insert_data)
Insert.place(x = 20,y = 300)

search = Button(root,text = "SEARCH",bg = "black",fg = "white",font = ("Arial",12),command = search_data)
search.place(x = 100,y = 300)

update = Button(root,text = "UPDATE",bg = "black",fg = "white",font = ("Arial",12),command = update_data)
update.place(x = 190,y = 300)

delete = Button(root,text = "DELETE",bg = "black",fg = "white",font = ("Arial",12),command = delete_data)
delete.place(x = 280,y = 300)

root.mainloop() 
