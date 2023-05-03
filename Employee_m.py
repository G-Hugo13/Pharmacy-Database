import mysql.connector
from connect_to_database import connect_to_database1



def create_employee_table():
    mydb = connect_to_database1()

    
    mycursor = mydb.cursor()

    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            employee_ID INT(5) UNSIGNED,
            name VARCHAR(25),
            phone_number VARCHAR(20), 
            PRIMARY KEY (employee_ID)
        )
    """)

    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS amount_returns (
            employee_ID INT(5) UNSIGNED,
            return_amount DECIMAL(10, 2),
            date_hired VARCHAR(10),
            FOREIGN KEY (employee_ID) REFERENCES employee(employee_ID)
        )
    """)
    
    employee_ID = input("Enter 5 digit employee ID: ")
    name = input("Enter employee name (First_Name Last_Name): ")
    phone_number = input("Enter employee phone number (numeric only, no symbols/letters): ")

    mycursor.execute("INSERT INTO employee (employee_ID, name, phone_number) VALUES (%s, %s, %s)", (employee_ID, name, phone_number))

    return_amount = input("Enter amount returned to date (no commas): $")
    date_hired = input("Enter the date of employment (MM-YYYY): ")

    mycursor.execute("INSERT INTO amount_returns (employee_ID, return_amount, date_hired) VALUES (%s, %s, %s)", (employee_ID, return_amount, date_hired))

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")




def view_employee():
    mydb = connect_to_database1()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM employee")

    rows = mycursor.fetchall()

    for row in rows:
        print(f"Employee_ID: {row[0]}\nName: {row[1]}\nPhone_number: {row[2]}\n")

    update_choice = input("Do you want to update an employee? (y/n): ")

    if update_choice.lower() == 'y':
        
        employee_ID = input("Enter employee ID to update: ")
        mycursor.execute("SELECT * FROM employee WHERE employee_ID = %s", (employee_ID,))

        row = mycursor.fetchone()
        
        if row:
            print(f"Current patient information: {row[1]}, {row[2]}")
            name = input("Enter new first and last name (leave blank to keep current value): ")
            phone_number = input("Enter new Phone Number (leave blank to keep current value): ")

            sql = "UPDATE employee SET name = %s, phone_number = %s WHERE employee_ID = %s"
            val = (name or row[1], phone_number or row[2], employee_ID)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record updated.")
        else:
            print("Employee not found.")
    



        

def view_cash_returns():
    mydb = connect_to_database1()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM amount_returns ORDER BY return_amount DESC")

    rows = mycursor.fetchall()
    
    for row in rows:
        print(f"Employee ID: {row[0]}\nAmount returned $: {row[1]}\nDate Hired: {row[2]}\n")

    update_choice = input("Do you want to update a report? (y/n): ")

    if update_choice.lower() == 'y':
        employee_ID = input("Enter employee ID: ")
        mycursor.execute("SELECT * FROM amount_returns WHERE employee_ID = %s", (employee_ID,))

        row = mycursor.fetchone()
        
        if row:
            print(f"Current report information: {row[1]}, {row[2]}")
            new_amount = input("Enter new amount: ")
            new_date = input("Enter new date (MM-YYYY): ")

            sql = "UPDATE amount_returns SET return_amount = %s, date_hired = %s WHERE employee_ID = %s"
            val = (new_amount or row[1], new_date or row[2], employee_ID)
            mycursor.execute(sql, val)
            
            
            mydb.commit()

            print("Returns report updated successfully.")
        
        else:
            print("Employee report not listed.")    



def employee_main():
    while True:
        print("------------------------")
        print("Employee Menu:")
        print("1. Admit new Employee")
        print("2. View/Edit Employee")
        print("3. View/Edit Employee Returns Report")
        print("4. EXIT")
        print("------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("------------------------")
            create_employee_table()
        elif choice == "2":
            print("------------------------")
            view_employee()
        elif choice == "3":
            print("------------------------")
            view_cash_returns()
        elif choice == "4":
            print("Exiting...")
            print("------------------------")
            break
        else:
            print("------------------------")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    employee_main()

  