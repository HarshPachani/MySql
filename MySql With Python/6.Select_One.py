import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Harsh@sql",
    database = "employee_data"
)

myCursor = db.cursor()
sql = "SELECT * FROM customers"
myCursor.execute(sql)

result = myCursor.fetchone()
print(result)
