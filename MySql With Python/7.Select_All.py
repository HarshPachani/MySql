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

results = myCursor.fetchall()

# print(result)
#for printing line by line, use for loop.
for data in results:
    print(data)
