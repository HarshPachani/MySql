import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Harsh@sql",
    database = "employee_data"
)

myCursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("Rekha", "Unknown", 8)

myCursor.execute(sql, val)

db.commit()
print("{} data changed.".format(myCursor.rowcount))