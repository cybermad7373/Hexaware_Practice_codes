CREATE DATABASE UniversityDB;
USE UniversityDB;
-- 1 nf
CREATE TABLE Student_Subjects (
    Student_ID INT,
    Subject VARCHAR(50),
    PRIMARY KEY (Student_ID, Subject)
);
-- 2 NF
CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(100)
);

CREATE TABLE Order_Products (
    Order_ID INT,
    Product_ID INT,
    Quantity INT,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID)
);
-- 3 NF
CREATE TABLE Departments_Normalized (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(100),
    Manager_ID INT
);

CREATE TABLE Employees_Normalized (
    Emp_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department_ID INT,
    FOREIGN KEY (Department_ID) REFERENCES Departments_Normalized(Department_ID)
);
-- 4NF 
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Courses (
    Course_ID INT PRIMARY KEY,
    Course_Name VARCHAR(100)
);

CREATE TABLE Enrollments (
    Student_ID INT,
    Course_ID INT,
    Enrollment_Date DATE NOT NULL,
    Grade VARCHAR(2),
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID),
    PRIMARY KEY (Student_ID, Course_ID)
);


/* ------------------- */
INSERT INTO Student_Subjects VALUES (1, 'Math'), (1, 'English'), (2, 'Science');
INSERT INTO Orders VALUES (101, 'Alice'), (102, 'Bob');
INSERT INTO Order_Products VALUES (101, 1, 2), (101, 2, 1), (102, 1, 1);
INSERT INTO Departments_Normalized VALUES (10, 'HR', 500), (20, 'IT', 501);
INSERT INTO Employees_Normalized VALUES (1, 'John', 10), (2, 'Jane', 20);
INSERT INTO Students VALUES (1, 'Ravi'), (2, 'Priya');
INSERT INTO Courses VALUES (101, 'Data Science'), (102, 'AI');
INSERT INTO Enrollments VALUES (1, 101, '2024-06-01', 'A'), (2, 102, '2024-06-02', 'B');

/* ------------------- */
SELECT Subject FROM Student_Subjects WHERE Student_ID = 1;

SELECT o.Order_ID, o.Customer_Name, op.Product_ID, op.Quantity
FROM Orders o
JOIN Order_Products op 
ON o.Order_ID = op.Order_ID;

SELECT e.Emp_ID, e.Name, d.Department_Name
FROM Employees_Normalized e
JOIN Departments_Normalized d 
ON e.Department_ID = d.Department_ID;

SELECT s.Name AS Student_Name, c.Course_Name, e.Enrollment_Date, e.Grade
FROM Enrollments e
JOIN Students s 
ON e.Student_ID = s.Student_ID
JOIN Courses c 
ON e.Course_ID = c.Course_ID;














