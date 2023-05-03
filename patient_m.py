import mysql.connector
import random
from connect_to_database import connect_to_database




def create_patient_profile():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS patients (patient_ID VARCHAR(5) PRIMARY KEY, pt_name VARCHAR(255), dob VARCHAR(10), gender VARCHAR(5), address VARCHAR(255), delivery VARCHAR(3), pt_phonenumber INT(10))")

    patient_ID = str(random.randint(10000, 99999))

    name = input("Enter patient name(First_Name Last_Name): ")
    dob = input("Enter patient DOB (mm-dd-yyyy): ")
    gender = input("Enter patient gender (M/F): ")
    address = input("Enter patient address: ")
    delivery= input("Delivery preffered (Y/N): ")
    pt_pn= input("Enter patients phone number: ")

    sql = "INSERT INTO patients (patient_ID, pt_name, dob, gender, address, delivery, pt_phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (patient_ID, name, dob, gender, address, delivery, pt_pn)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    


def view_all_patients():
    mydb = connect_to_database()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM patients")

    rows = mycursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}\nName: {row[1]}\nDob: {row[2]}\nGender: {row[3]}\nAddress: {row[4]}\nDelivery: {row[5]}\nPhone Number: {row[6]}\n")

    update_choice = input("Do you want to update a patient? (y/n): ")

    if update_choice.lower() == 'y':
        
        patient_ID = input("Enter patient ID to update: ")
        mycursor.execute("SELECT * FROM patients WHERE patient_ID = %s", (patient_ID,))

        row = mycursor.fetchone()
        
        if row:
            print(f"Current patient information: {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")
            name = input("Enter new first and last name (leave blank to keep current value): ")
            dob = input("Enter new DOB (leave blank to keep current value): ")
            gender = input("Enter new gender (leave blank to keep current value): ")
            address = input("Enter new address (leave blank to keep current value): ")
            delivery= input("Enter new delivery preference (leave blank to keep current value): ")
            pt_pn= input("Enter new phone number (leave blank to keep current value): ")

            sql = "UPDATE patients SET pt_name = %s, dob = %s, gender = %s, address = %s, delivery =%s, pt_phonenumber =%s WHERE patient_ID = %s"
            val = (name or row[1], dob or row[2], gender or row[3], address or row[4], delivery or row[5], pt_pn or row[6],  patient_ID)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record updated.")
        
        else:
            print("Patient not found.")
    

        



def pt_main():
    while True:
        print("------------------------")
        print("Profile Menu")
        print("1. Create a patient profile")
        print("2. View/Edit patient profiles")
        print("3. EXIT")
        print("------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("------------------------")
            create_patient_profile()
        elif choice == "2":
            print("------------------------")
            view_all_patients()
        elif choice == "3":
            print("Exiting...")
            print("------------------------")
            break
        else:
            print("------------------------")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    pt_main()