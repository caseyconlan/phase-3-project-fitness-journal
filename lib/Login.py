# database.py
from models import Base
target_metadata = Base.metadata
from lib.Loginform import Database
import mysql.connector as mysql
# Create a database connection

mydb = mysql.connector.connect(
host="localhost",
user = "yourusername",
password = "yourpassword",
database = "mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES") #This is to test out the database I think casey already technically created one but I am adding this one to make sure this is whats usually supposed to be in one of our files is what I read on a Python project database website this is the tesing part the words in parenthesis change and the print will be deleted I think I have to do some of the steps I may I have missed on Monday.

for x in mycursor:
    print(x)

