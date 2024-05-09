# TKinter Demo

from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Registration Form - From Tkinter Example")
root.resizable(width=False,height = False)

l_id = Label(root,text = "ID")
l_id.place(x=50,y=50)

l_fName = Label(root,text = "First name")
l_fName.place(x=50,y=100)

l_lName = Label(root,text = "Last Name")
l_lName.place(x=50,y=150)

l_email = Label(root,text = "Email")
l_email.place(x=50,y=200)

l_mobile = Label(root,text = "Mobile Number")
l_mobile.place(x=50,y=250)

# User Input

e_id = Entry(root)
e_id.place(x=200,y=50)

e_fName = Entry(root)
e_fName.place(x=200,y=100)

e_lName = Entry(root)
e_lName.place(x=200,y=150)

e_email = Entry(root)
e_email.place(x=200,y=200)

e_mobile = Entry(root)
e_mobile.place(x=200,y=250)

# Button

Insert = Button(root,text = "INSERT",bg = "black",fg = "white",font = ("Arial",12))
Insert.place(x = 20,y = 300)

Insert = Button(root,text = "SEARCH",bg = "black",fg = "white",font = ("Arial",12))
Insert.place(x = 100,y = 300)

Insert = Button(root,text = "UPDATE",bg = "black",fg = "white",font = ("Arial",12))
Insert.place(x = 190,y = 300)

Insert = Button(root,text = "DELETE",bg = "black",fg = "white",font = ("Arial",12))
Insert.place(x = 280,y = 300)











