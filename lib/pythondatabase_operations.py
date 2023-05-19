 #!/usrbin/python  

from multiprocessing import connection
import sqlite3
from openstack import connect
from prettytable import PrettyTable

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_data(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close() 
    
def display_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Username", "Password"]

    for row in rows:
        table.add_row(row)

    # Customize table styling
    table.align = "l"
    table.padding_width = 2
    table.header_style = "upper"
    table.horizontal_char = "-"
    table.vertical_char = "|"
    table.junction_char = "+"
    table.border = True

    # Customize table formatting using ANSI escape sequences
    table.format = True
    table.int_format = "s"
    
    # Print the logo as the header
logo = "\033[3;30;47mLift A Ton\033[0m"
print(logo)
print("\nTable Contents:")
print("\033[1;34m" + str(table) + "\033[0m")

    # Print the table with styling
print("\033[1;34m" + str(table) + "\033[0m")

connection.close()

def main():
    create_table()

    while True:
        print("1. Insert data")
        print("2. Display table")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            insert_data(username, password)
            print("Data inserted successfully!")
        elif choice == '2':
            display_table()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 

#I am not done with this form have to include sign up as well tommorrow or during the weekend. Please provide me with a to do list over the weekend.


# # Create a register form tomorrow did not create table yet would not allow me to in my cli line or I was doing it wrong but main s calling as the top of the tree.

# I can hide the passwords and create that with this due to the fact of all my vs errors I am not adding until I get fixed tomorrow and we decide which one we go with. I have to fix what I had to download for the other one that I thought I didn't I accidentally downloaded the wrong one and messed up my system because I stayed up too late and started making errors. 
