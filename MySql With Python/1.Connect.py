import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Harsh@sql"
)

if db.is_connected():
    print("Database Conncected.")