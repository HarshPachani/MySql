import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Database Password Here",
    database = "employee_data"
)

myCursor = db.cursor()
sql = """CREATE TABLE customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
)
"""
myCursor.execute(sql)

print("Table Created Successful !!!")