# Loan Management System

A Python-based application for managing loans, customers, and loan processing with MySQL database integration.

# CHeck for output of the program [click here](https://github.com/cybermad7373/Hexaware_Practice_codes/wiki/Python-Coding-challenge-Output)

## Features

- Customer management (create, view, update)
- Loan processing (Home loans and Car loans)
- Interest and EMI calculations
- Loan status tracking (Pending/Approved/Rejected)
- Database persistence for all entities
- Comprehensive test coverage

## Prerequisites

- Python 3.10+
- MySQL Server 8.0+
- MySQL Connector/Python
- pytest (for testing)

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/cybermad7373/loan-management-system.git
cd loan-management-system
```
2. **Create and activate a virtual environment**:

python -m venv .venv
.\.venv\Scripts\activate            # Windows

3. **Install the required packages**:
```pip install -r requirements.txt```

4. **Running the Application**:
```bash
python -m main.main_module
```
5. **Testing**:
```bash
pytest -v
```

***

Usage Examples:

Applying for a Home Loan:
Select "Apply for a Loan" from the main menu
Choose "Home Loan"
Enter customer details and loan information
Confirm the application

Checking Loan Status:
Select "Check Loan Status" from the main menu
Enter the Loan ID
View approval status based on credit score

Making a Payment:
Select "Make Loan Repayment"
Enter Loan ID and payment amount
System calculates how many EMIs can be paid

Key configuration files:
database/db.properties - Database connection settings
util/db_conn_util.py - Connection management

Troubleshooting
Common Issues
Database Connection Errors:
Verify MySQL service is running
Check credentials in db.properties
Ensure database and tables exist

Import Errors:
Make sure all __init__.py files exist
Run from project root directory
Try pip install -e . to install in development mode

Test Failures:
Ensure test database is properly set up
Check for any pending migrations
Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request
