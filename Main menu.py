from patient_m import pt_main
from inventory_m import inventory_menu
from Employee_m import employee_main


def Menu():
    while True:
        print("------------------------")
        print("Main Menu")
        print("1. Patient Profiles")
        print("2. Inventory")
        print("3. Employee Information")
        print("4. Exit")
        print("------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("------------------------")
            pt_main()
        elif choice == "2":
            print("------------------------")
            inventory_menu()
        elif choice == "3":
            print("------------------------")
            employee_main()
            print("------------------------")
        elif choice == "4":
            print("Exiting...")
            print("------------------------")
            break
        else:
            print("------------------------")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Menu()