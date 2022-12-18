import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Database Password Here"
)

thisCursor = db.cursor()
thisCursor.execute("CREATE DATABASE employee_data")

print("Database Created Successfully!!")