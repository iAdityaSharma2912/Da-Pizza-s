# Da-Pizza-s

# Pizza Restaurant Management System Installation Guide

## Project Details
- **Project Name:** Da Pizza's
- **Creator Name:** Aditya Sharma

## System Requirements
- Python 3.x installed on your system
- MySQL installed on your system
- Basic understanding of Python and MySQL

## Installation Steps
1. **Clone the Repository**: 
   - Clone the repository from [GitHub Repository Link](#).
   - Alternatively, you can download and extract the ZIP file.

2. **Install Dependencies**:
   - Make sure you have `mysql-connector-python` installed.
   - You can install it using pip:
     ```
     pip install mysql-connector-python
     ```

3. **Database Setup**:
   - Open MySQL and run the following commands to set up the database:
     ```sql
     CREATE DATABASE resturant;
     USE resturant;
     CREATE TABLE login_details (
         Username VARCHAR(20) UNIQUE NOT NULL,
         Password VARCHAR(20) UNIQUE NOT NULL,
         Designation VARCHAR(20)
     );
     INSERT INTO login_details VALUES ('owner', 'owner@123', 'owner');
     -- Additional SQL commands as per the provided Python script.
     ```

4. **Run the Application**:
   - Run the Python script (`pizza_management.py`) to start the application:
     ```
     python pizza_management.py
     ```

## Accessing the Application
- Upon running the script, you'll be prompted with a menu to choose your role: Customer, Owner, or Delivery Boy.
- Use the following credentials for owner login:
  - Username: owner
  - Password: owner@123

## Support
For any issues or queries regarding the installation process or application functionality, feel free to contact us.
