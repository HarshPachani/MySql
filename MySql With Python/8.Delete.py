import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Database Password Here",
    database = "employee_data"
)

myCursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id = %s"
val = (1, )
myCursor.execute(sql, val)

db.commit()
print("{} data deleted.".format(myCursor.rowcount))