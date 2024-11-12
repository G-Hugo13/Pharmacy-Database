"""
# Pharmacy Database Project

## Author
Hugo Gonzalez  
CYBI-6315-01-Spring2023  

## Project Overview
The Pharmacy Database Project is designed to enhance pharmacy operations by focusing on revenue growth 
and improved patient experience. Drawing from five years of experience at CVS, the project addresses 
common issues in independent pharmacies, such as outdated software, customer retention, and inventory 
management challenges.

## Purpose
This project offers a software solution to manage patient, employee, and inventory data while enabling 
report generation for auditing and editing. Using MySQL as the primary database and Python as the interface, 
this program provides an intuitive way for users to access various records with restricted access through user roles.

## Technologies Used
- MySQL: For storing, creating, and managing data tables.
- Python: For bridging interactions between users and the MySQL database.
- MySQL Workbench: To build and manage the Pharmacy Database.

## Database Structure
The Pharmacy database is structured around five main entities:
1. Patients: Stores patient details such as ID, name, date of birth, address, delivery preferences, and phone number.
2. Employees: Contains employee records, including ID, name, and phone number.
3. Returns Amount: Tracks employee return amounts and hire dates, linked to the employee table.
4. Inventory: Manages items in stock, including ID, description, unit price, and quantity.
5. Inventory Balance: Monitors inventory balances linked to the inventory table.

## Functionalities
1. User Access Control: Users, such as Technicians and Pharmacists, are created in MySQL with privileges 
   to access specific database functions.
2. Patient Management: Create and view patient profiles. Each profile includes essential details stored 
   in the patients' table.
3. Employee Management: Manage employee records and returns reports, with exclusive access for administrators.
4. Inventory Management: Add and view inventory items, with profit calculations based on unit price and quantity.
5. Reports and Queries: Generate reports, such as inventory profit reports, patient information filtered 
   by location, and employee returns.

![image](https://github.com/user-attachments/assets/0e29586d-db75-49f0-a19b-19fe6c730cb4)

![image](https://github.com/user-attachments/assets/1050f2e1-4ce8-4d38-887f-5b62205c9e3b)

![image](https://github.com/user-attachments/assets/94e298c4-88e1-4199-bd6e-2084b3f84e04)


## Methodology
1. Database Creation: A MySQL database named "Pharmacy" is set up, with user roles assigned access privileges.
2. Python Functions:
   - Database Connection: A connection file (`connect_to_database.py`) validates users against MySQL credentials.
   - Patient Profiles: A Python file for managing patient data, with functions to create and view patient profiles.
   - Employee and Inventory Menus: Separate menus for employee and inventory management with options for adding, 
     viewing, and editing records.

## Limitations and Future Work
- Currently, the program operates locally using Python and MySQL.
- Potential improvements include deploying this project to a web application with features like automated refill 
  reminders and medication history tracking.

## Conclusion
The Pharmacy Database Project is a fully functional, user-friendly program for managing patient, employee, 
and inventory data. Its security features ensure that only authorized users can access specific information, 
and the structured menus guide users through tasks with ease. This project serves as a valuable template for 
implementing pharmacy database management systems focused on improving workflow and patient satisfaction.
"""
