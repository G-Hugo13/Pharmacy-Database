import mysql.connector
from connect_to_database import connect_to_database
from connect_to_database import connect_to_database1


def create_tables_and_input_data():
    mydb = connect_to_database()
    
    cursor = mydb.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS inventory (id INT(8) PRIMARY KEY, item VARCHAR(255), unit_price FLOAT, quantity FLOAT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS profit (id INT(8), balance FLOAT, FOREIGN KEY (id) REFERENCES inventory(id))")

    mydb.commit()

    while True:
        id_num = int(input("Enter the 8 digit ID number: "))
        item = input("Enter the medication name & strength: ")
        unit_price = float(input("Enter the unit price: $"))
        quantity = float(input("Enter the quantity in stock: "))

        cursor.execute("INSERT INTO inventory (id, item, unit_price, quantity) VALUES (%s, %s, %s, %s)", (id_num, item, unit_price, quantity))

        balance = unit_price * quantity
        cursor.execute("INSERT INTO profit (id, balance) VALUES (%s, %s)", (id_num, balance))

        print("------------------------")
        another_item = input("Do you want to enter data for another item? (y/n): ")

        if another_item.lower() == "n":
            break

    mydb.commit()

    mydb.close()



def view_inventory_table():
    mydb = connect_to_database()

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM inventory")

    rows = cursor.fetchall()

    print("ID\tItem\tUnit Price\tQuantity")
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

    mydb.close()
    print("------------------------")
    choice = input("Do you want to make an update? (y/n): ")
    if choice.lower() == "y":
        update_inventory_table()
        
        
        


def update_inventory_table():
    mydb = connect_to_database()

    cursor = mydb.cursor()

    id = input("Enter the ID of the medication you want to update: ")

    cursor.execute(f"SELECT * FROM inventory WHERE id = {id}")

    row = cursor.fetchone()

    if row:
        item = input("Enter the new name & strength (leave blank to keep current value): ")
        if item == "":
            item = row[1]  
        unit_price = input("Enter the new unit price of the medication (leave blank to keep current value): ")
        if unit_price == "":
            unit_price = row[2]  
        else:
            unit_price = float(unit_price)

        quantity = input("Enter the new quantity of the medication (leave blank to keep current value): ")
        if quantity == "":
            quantity = row[3]  
        else:
            quantity = float(quantity)

        cursor.execute(f"UPDATE inventory SET item = '{item}', unit_price = {unit_price}, quantity = {quantity} WHERE id = {id}")

        mydb.commit()

        balance = unit_price * quantity
        cursor.execute(f"UPDATE profit SET balance = {balance} WHERE id = {id}")
        mydb.commit()

        print(f"Medication with ID {id} has been updated.")
    else:
        print(f"Medication with ID {id} does not exist in the inventory table.")

    mydb.close()


def view_profit_table():
    mydb = connect_to_database1()

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM profit ORDER BY balance DESC")

    rows = cursor.fetchall()

    if rows:
        print("ID\tBalance")
        print("-" * 20)
        for row in rows:
            print(f"{row[0]}\t{row[1]}")
    else:
        print("There are no rows in the profit table.")

    mydb.close()











def inventory_menu():
    while True:
        print("------------------------")
        print("Inventory Menu")
        print("1. Add inventory")
        print("2. View inventory report")
        print("3. View profit report")
        print("4. Exit")
        print("------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("------------------------")
            create_tables_and_input_data()
        elif choice == "2":
            print("------------------------")
            view_inventory_table()
        elif choice == "3":
            print("------------------------")
            view_profit_table()
            print("------------------------")
        elif choice == "4":
            print("Exiting...")
            print("------------------------")
            break
        else:
            print("------------------------")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    inventory_menu()