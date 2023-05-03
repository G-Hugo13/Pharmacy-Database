import mysql.connector


def connect_to_database1():
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    print("Connecting...")
    if username == "Pharmacist":
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="pharmacy"
        )
        return mydb
    
    print("Access denied.")
    return exit()


def connect_to_database():
    username = input("Enter username: ")
    password = input("Enter password: ")

    print("Connecting...")
    
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user=username,
          password=password,
          database="pharmacy"
        )
    except mysql.connector.Error:
        print("Invalid Credentials")
        return exit()

    return mydb
