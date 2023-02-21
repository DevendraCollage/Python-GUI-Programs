# Import the tkinter module
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
# this is the button command
import delete as DELETE
import update as UPDATE
# Import the database connection module
import mysql.connector as mysql

# GUI Part
root = Tk()
root.geometry("900x600")  # This is the size of the GUI Screen
# Global Variables
global e1
global e2
global e3
global e4

# Heading
tk.Label(root, text="Student Registration", fg="black", font=(None, 30)).place(x=515, y=10)

# Field Label
tk.Label(root, text="Student ID").place(x=10, y=10)
Label(root, text="Student Name").place(x=10, y=40)
Label(root, text="Course").place(x=10, y=70)
Label(root, text="Fees").place(x=10, y=100)

# Edit Text Box
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

# Three button (Add, Button, Delete)
Button(root, text="Insert", command=INSERT, height=3, width=13, bg="yellow").place(x=30, y=150)
Button(root, text="Update", command=UPDATE, height=3, width=13, bg="yellow").place(x=150, y=150)
Button(root, text="Delete", command=DELETE, height=3, width=13, bg="yellow").place(x=270, y=150)

# This is for grid layout
cols = ("Id", "Name", "Course", "Fees")
listbox = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=2)
    listbox.place(x=20, y=260)

listbox.bind('<Double-Button-1>', INSERT)
root.mainloop()  # This is use for display the screen


# Backend Part
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['name'])
    e3.insert(0, select['course'])
    e4.insert(0, select['fees'])


# This function is for Insert Data into the Database through GUI Form
def Add():
    studid = e1.get()
    studname = e2.get()
    course = e3.get()
    fee = e4.get()
    e1.focus_set()
    # Open Database Connection
    db = mysql.connect(host="localhost", user="root", password="", database="GEETANJALI")
    # Create cursor object using cursor() method
    cursor = db.cursor()

    try:
        # SQL Query
        sql = """INSERT INTO BCA
                 (ID,SNAME,COURSE,FEE)
                 VALUES (%s,%s,%s,%s)"""
        val = (studid, studname, course, fee)
        # Execute the cursor method
        data = cursor.execute(sql, val)
        # Commit in the database
        db.commit()
        lastid = data.lastrowid
        messagebox.showinfo("information", "Student Inserted Successfully!")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        # Rollback in the database
        db.rollback()
        # Close Database Connection
        db.close()


# This function is for Update Data in the Database through GUI Form
def update():
    studid = e1.get()
    studname = e2.get()
    course = e3.get()
    fee = e4.get()
    # Open Database Connection
    db = mysql.connect(host="localhost", user="root", password="", database="GEETANJALI")
    # Create Cursor object using cursor() method
    cursor = db.cursor()

    try:
        # SQL Query
        sql = "UPDATE BCA SET SNAME=%s,COURSE=%s,FEE=%s where ID=%s"
        val = (studid, studname, course, fee)
        # Execute the cursor() method
        data = cursor.execute(sql, val)
        # Commit in the database
        db.commit()
        lastid = data.lastrowid
        messagebox.showinfo("information", "Record Updated Successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        # Rollback in the database
        db.rollback()
        # Close Database Connection
        db.close()


def delete():
    studid = e1.get()
    # Open Database Connection
    db = mysql.connect(host="localhost", user="root", password="", database="GEETANJALI")
    # Create cursor object using cursor() method
    cursor = db.cursor()

    try:
        # SQL Query
        sql = "DELETE FROM BCA where ID=%s"
        val = (studid)
        # Execute the cursor method
        data = cursor.execute(sql, val)
        # Commit in the database
        db.commit()
        lastid = data.lastrowid
        messagebox.showinfo("information", "Record Deleted Successfully!")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        # Rollback in the Database
        db.rollback()
        # Close Database Connection
        db.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="GEETANJALI")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,sname,course,fee FROM BCA")
    records = mycursor.fetchall()
    print(records)

    for i, (id, sname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, sname, course, fee))
        mysqldb.close()
