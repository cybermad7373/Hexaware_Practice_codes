# Student Information System (SIS)

This **Student Information System (SIS)** is a modular Python application designed to manage student records, courses, enrollments, teachers, and payments in an educational institution. It follows a clean architecture with separation of concerns to ensure maintainability and scalability.

---

## 🚀 Features

✅ **Student Management:** Create, read, update, and delete student records  
✅ **Course Management:** Manage course offerings and details  
✅ **Enrollment System:** Handle student enrollments with validation  
✅ **Teacher Management:** Maintain teacher information  
✅ **Payment Processing:** Process and track student payments  
✅ **Exception Handling:** Comprehensive custom exceptions for robust error handling  
✅ **Database Utilities:** Secure database connection management  
✅ **Validation:** Input validation utilities

---

## 📂 Project Structure
```
sis/
├── config/
│   └── db_config.ini
├── dao/
│   ├── __init__.py
│   ├── sis_service.py
│   └── sis_service_impl.py
├── entity/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── enrollment.py
│   ├── teacher.py
│   └── payment.py
├── exception/
│   ├── __init__.py
│   ├── duplicate_enrollment_exception.py
│   ├── course_not_found_exception.py
│   ├── student_not_found_exception.py
│   ├── teacher_not_found_exception.py
│   ├── payment_validation_exception.py
│   └── insufficient_funds_exception.py
├── util/
│   ├── __init__.py
│   ├── db_conn_util.py
│   ├── db_property_util.py
│   ├── security_util.py
│   └── validation_util.py
├── test/
│   ├── __init__.py
│   ├── test_exceptions.py
│   ├── test_student_management.py
│   ├── test_course_management.py
│   ├── test_enrollment_management.py
│   └── test_payment_management.py
└── main.py
```

---

## ⚙️ Prerequisites

- Python **3.8+**
- MySQL Database (or compatible RDBMS)
- Python packages listed in `requirements.txt`

---


### Documentation Overview
Entity Layer: Core domain objects (e.g., Student, Course, Enrollment).

DAO Layer: Handles all database operations (CRUD, queries).

Service Layer: Implements business logic, interacting with the DAO.

Utilities: Reusable helper functions (DB connections, security, validation).

Exception Handling: Custom exceptions for precise error control.

