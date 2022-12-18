import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Database Password Here",
    database = "employee_data"
)

myCursor = db.cursor()
# myCursor.execute("USE employee_data")
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
values = [ #This is List Class.
    ("Kunj", "Gandhinagar"),
    ("Toral", "Gandhinagar"),
    ("Devanshu", "Ahmedabad"),
    ("Nirav", "Adalaj"),
]
# print(type(values))
for val in values:
    myCursor.execute(sql, val)

db.commit()

print("{} data added.".format(myCursor.rowcount))