import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Database Password Here",
    database = "employee_data"
)

myCursor = db.cursor()

sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = ("Harsh", "Ahmedabad")
myCursor.execute(sql, val)

db.commit() #For Inserting the data to the database.

#To print the number of data added.
print("{} data added".format(myCursor.rowcount))