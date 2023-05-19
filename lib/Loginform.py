from logging import root
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

# Create a database connection
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)"
    )

# Assign variables
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
click_button = StringVar()

# Create a login form
def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(
        LoginFrame,
        text="Username:",
        font=("arial", 25),
        bd=18,
    )
    lbl_username.grid(row=1)
    lbl_password = Label(
        LoginFrame,
        text="Password:",
        font=("arial", 25),
        bd=18,
    )
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=("arial", 18))
    lbl_result1.grid(row=3, column_span=2)
    username = Entry(
        LoginFrame,
        text = USERNAME,
        font=("arial", 20),
        width=15,
    )
    username.grid(row=1, column=1)
    password = Entry(
        LoginFrame,
        text = PASSWORD,
        font=("arial", 20),
        width=15,
        show="*",
    )
    password.grid(row=2, column=1)
    btn_login = Button(
        LoginFrame,
        text="Login",
        font=("arial", 18),
        width=35,
        command=Login,
    )
    btn_login.grid(row=4, column_span=2, pady=20)
    lbl_register = Label(
        LoginFrame,
        text="Register",
        fg="Blue",
        font=("arial", 12),
    )
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind("<Button-1>", click_button)

# Create a register form
def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(
        RegisterFrame,
        text="Username:",
        font=("arial", 18),
        bd=18,
    )
    lbl_username.grid(row=1)
    lbl_password = Label(
        RegisterFrame,
        text="Password:",
        font=("arial", 18),
        bd=18,
    )
    lbl_password.grid(row=2)
    lbl_firstname = Label(
        RegisterFrame,
        text="Firstname:",
        font=("arial", 18),
        bd=18,
    )
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(
        RegisterFrame,
        text="Lastname:",
        font=("arial", 18),
        bd=18,
    )
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=("arial", 18))
    lbl_result2.grid(row=5, column_span=2)
    username = Entry(
        RegisterFrame,
        text = USERNAME,
        font=("arial", 20),
        width=15,
    )
    username.grid(row=1, column=1)
    password = Entry(
        RegisterFrame,
        text = PASSWORD,
        font=("arial", 20),
        width=15,
        show="*",
    )
    password.grid(row=2, column=1)
    firstname = Entry(
        RegisterFrame,
        text = FIRSTNAME,
        font=("arial", 20),
        width=15,
    )
    firstname.grid(row=3, column=1)
    lastname = Entry(
        RegisterFrame,
        text = LASTNAME,
        font=("arial", 20),
        width=15,
    )
    lastname.grid(row=4, column=1)
    
# Create a function for validating the login input
def Login():
    Database() # Connect to the database
    if USERNAME.get() == "" or PASSWORD.get() == "": # Check if any field is empty
        lbl_result1.config(text="Please complete the required field!", fg="red")
    else:
      cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get())) # Query the database for matching username and password
    if cursor.fetchone() is not None: # If there is a match
        lbl_result1.config(text="You Successfully Login!", fg="blue")
# Do something after login success
    else: # If there is no match
        lbl_result1.config(text="Invalid Username or password", fg="red")
    USERNAME.set("") # Clear the username field
    PASSWORD.set("") # Clear the password field
    cursor.close() # Close the cursor
    conn.close() # Close the connection

    if __name__ == "__main__":
        main() 
#I believe it decided to add this one to the database instead I could be wrong but the main means the main branch 
