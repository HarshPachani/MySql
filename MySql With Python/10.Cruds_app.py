import mysql.connector
import os

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Harsh@sql",
    database = "employee_data"
)

def insert_data(db):
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    myCursor = db.cursor()
    sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
    value = (name, address)
    myCursor.execute(sql, value)
    db.commit()
    print("{} data Inserted.".format(myCursor.rowcount))

def show_data(db):
    myCursor = db.cursor()
    sql = "SELECT * FROM customers"
    myCursor.execute(sql)
    results = myCursor.fetchall()

    if myCursor.rowcount <= 0:
        print("There is not any data found!!")
    else:
        for data in results:
            print(data)

def update_data(db):
    myCursor = db.cursor()
    show_data(db)
    customer_id = input("Enter Customer Id: ")
    name = input("New Name: ")
    address = input("New Address: ")

    sql = "UPDATE customers SET name = %s, address = %s WHERE customer_id = %s"
    val = (name, address, customer_id)
    myCursor.execute(sql, val)
    db.commit()
    print("{} data Successfully Changed.".format(myCursor.rowcount))

def delete_data(db):
    myCursor = db.cursor()
    show_data(db)
    customer_id = input("Enter Customer Id: ")
    sql = "DELETE FROM customers WHERE customer_id = %s"
    val = (customer_id, )
    myCursor.execute(sql, val)
    db.commit()
    print("{} data Successfully Deleted.".format(myCursor.rowcount))

def search_data(db):
    myCursor = db.cursor()
    keyword = input("Keyword: ")
    sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    myCursor.execute(sql, val)
    results = myCursor.fetchall()

    if myCursor.rowcount <= 0:
        print("There is not any data found!!")
    else:
        for data in results:
            print(data)

def showMenu(db):
    print("==========APPLICATION DATABASE PYTHON=========")
    print("1. Insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Search data")
    print("0. Exit")
    print("-------------------")
    menu = input("Choose menu> ")

    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    else:
        exit()
if __name__ == "__main__":
    while(True):
        showMenu(db)