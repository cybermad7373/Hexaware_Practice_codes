project_portfolio/
├── expense_tracker/
│   ├── __init__.py
│   ├── expense_tracker.py
│   ├── expense_db.py
│   ├── lld.md
│   └── test_expense.py
├── student_report/
│   ├── __init__.py
│   ├── report_card.py
│   ├── student_db.py
│   ├── lld.md
│   └── test_report.py
├── quiz_app/
│   ├── __init__.py
│   ├── quiz.py
│   ├── quiz_db.py
│   ├── lld.md
│   └── test_quiz.py
├── bill_splitter/
│   ├── __init__.py
│   ├── splitter.py
│   ├── splitter_db.py
│   ├── lld.md
│   └── test_splitter.py
├── database/
│   ├── __init__.py
│   ├── db_connection.py
│   └── schema.sql
├── requirements.txt
└── README.md

Implementation Notes

Each project has its own module with:
Main functionality class
Database handler class
LLD documentation
Test file
Database connectivity is centralized in the database folder with:
Connection singleton class
Schema creation script
Environment variables for configuration

Key features implemented:
Expense tracking with monthly/yearly summaries
Student report card generation with grade calculation
Quiz application with score tracking
Bill splitting with item-level sharing

Python concepts used across projects:
Object-oriented programming
Lambda functions
List/dictionary comprehensions
Type hints
Datetime operations
Math calculations

To set up the project:
Create a MySQL database
Set up environment variables in a .env file
Run schema.sql to create tables
Install requirements with pip install -r requirements.txt
Run individual project files or create a main.py to integrate all projects