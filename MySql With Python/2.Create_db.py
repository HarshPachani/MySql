import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Harsh@sql"
)

thisCursor = db.cursor()
thisCursor.execute("CREATE DATABASE employee_data")

print("Database Created Successfully!!")