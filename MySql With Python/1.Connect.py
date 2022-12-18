import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Database Password Here"
)

if db.is_connected():
    print("Database Conncected.")