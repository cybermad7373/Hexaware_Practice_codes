-- Database creation
CREATE DATABASE IF NOT EXISTS SISDB;
USE SISDB;

-- Students table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Teachers table
CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_teacher_email CHECK (email LIKE '%@%.%')
);

-- Courses table
CREATE TABLE IF NOT EXISTS Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) NOT NULL UNIQUE,
    credits INT NOT NULL,
    teacher_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id) ON DELETE SET NULL,
    CONSTRAINT chk_credits CHECK (credits > 0 AND credits <= 6)
);

-- Enrollments table
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (student_id, course_id)
);

-- Payments table
CREATE TABLE IF NOT EXISTS Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount CHECK (amount > 0)
);

-- Insert Indian teachers data
INSERT INTO Teachers (first_name, last_name, email) VALUES
('Ragavi', 'Venugopal', 'ragavi.venugopal@university.edu'),
('Amith', 'Kumar', 'amith.kumar@university.edu'),
('Kavin', 'Kumar', 'kavin.kumar@university.edu'),
('Ranjith', 'Kumar', 'ranjith.kumar@university.edu'),
('Sreya', 'Goshal', 'sreya.goshal@university.edu');

-- Insert Indian students data (passwords are hashed versions of 'student123')
INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number, password_hash) VALUES
('Ruthra', 'Varshan', '2000-05-15', 'ruthra.varshan@student.edu', '9876543210', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Ragavi', 'Venugopal', '1999-11-22', 'ragavi.venugopal@student.edu', '9876543211', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Amith', 'Kumar', '2001-03-08', 'amith.kumar@student.edu', '9876543212', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Kavin', 'Kumar', '2000-07-19', 'kavin.kumar@student.edu', '9876543213', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Ranjith', 'Kumar', '1999-09-30', 'ranjith.kumar@student.edu', '9876543214', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Sreya', 'Goshal', '2001-01-12', 'sreya.goshal@student.edu', '9876543215', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Priya', 'Dharshini', '2000-08-25', 'priya.dharshini@student.edu', '9876543216', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Arjun', 'Reddy', '1999-12-05', 'arjun.reddy@student.edu', '9876543217', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Divya', 'Prakash', '2001-02-18', 'divya.prakash@student.edu', '9876543218', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09'),
('Vijay', 'Sethupathi', '2000-06-21', 'vijay.sethupathi@student.edu', '9876543219', '$pbkdf2-sha512$25000$N2Y5MWU0ZGQ2ODAwMDAwMA$VW9vZ0h1R1VqSmdQb2VhL1F6QnJjZz09');

-- Insert courses data
INSERT INTO Courses (course_name, course_code, credits, teacher_id) VALUES
('Introduction to Computer Science', 'CS101', 3, 1),
('Calculus I', 'MATH101', 4, 2),
('English Composition', 'ENG101', 3, 3),
('Physics Fundamentals', 'PHYS101', 4, 4),
('Database Systems', 'CS302', 3, 1),
('Advanced Mathematics', 'MATH301', 4, 2),
('Literature Survey', 'ENG201', 3, 3),
('Quantum Physics', 'PHYS301', 4, 4),
('Software Engineering', 'CS401', 3, 5),
('Artificial Intelligence', 'CS402', 3, 5);

-- Insert enrollments data
INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2023-01-10'), (1, 2, '2023-01-10'), (1, 3, '2023-01-10'),
(2, 1, '2023-01-11'), (2, 4, '2023-01-11'), (2, 5, '2023-01-11'),
(3, 2, '2023-01-12'), (3, 3, '2023-01-12'), (3, 6, '2023-01-12'),
(4, 4, '2023-01-13'), (4, 5, '2023-01-13'), (4, 7, '2023-01-13'),
(5, 1, '2023-01-14'), (5, 6, '2023-01-14'), (5, 8, '2023-01-14'),
(6, 2, '2023-01-15'), (6, 7, '2023-01-15'), (6, 9, '2023-01-15'),
(7, 3, '2023-01-16'), (7, 8, '2023-01-16'), (7, 10, '2023-01-16'),
(8, 4, '2023-01-17'), (8, 9, '2023-01-17'), (8, 1, '2023-01-17'),
(9, 5, '2023-01-18'), (9, 10, '2023-01-18'), (9, 2, '2023-01-18'),
(10, 6, '2023-01-19'), (10, 1, '2023-01-19'), (10, 3, '2023-01-19');

-- Insert payments data
INSERT INTO Payments (student_id, amount, payment_date) VALUES
(1, 5000.00, '2023-01-05'), (1, 3000.00, '2023-02-10'),
(2, 6000.00, '2023-01-06'), (2, 4000.00, '2023-02-11'),
(3, 5500.00, '2023-01-07'), (3, 3500.00, '2023-02-12'),
(4, 7000.00, '2023-01-08'), (4, 2000.00, '2023-02-13'),
(5, 4500.00, '2023-01-09'), (5, 2500.00, '2023-02-14'),
(6, 8000.00, '2023-01-10'), (6, 1000.00, '2023-02-15'),
(7, 6500.00, '2023-01-11'), (7, 1500.00, '2023-02-16'),
(8, 7500.00, '2023-01-12'), (8, 500.00, '2023-02-17'),
(9, 9000.00, '2023-01-13'), (9, 750.00, '2023-02-18'),
(10, 8500.00, '2023-01-14'), (10, 1250.00, '2023-02-19');

-- Create views for common queries
CREATE VIEW StudentEnrollmentView AS
SELECT s.student_id, CONCAT(s.first_name, ' ', s.last_name) AS student_name,
       c.course_id, c.course_name, e.enrollment_date
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

CREATE VIEW CourseEnrollmentCount AS
SELECT c.course_id, c.course_name, COUNT(e.student_id) AS enrollment_count
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- Create stored procedures
DELIMITER //
CREATE PROCEDURE GetStudentPayments(IN student_id_param INT)
BEGIN
    SELECT p.payment_id, p.amount, p.payment_date
    FROM Payments p
    WHERE p.student_id = student_id_param
    ORDER BY p.payment_date DESC;
END //

CREATE PROCEDURE GetCourseStudents(IN course_id_param INT)
BEGIN
    SELECT s.student_id, CONCAT(s.first_name, ' ', s.last_name) AS student_name,
           s.email, e.enrollment_date
    FROM Students s
    JOIN Enrollments e ON s.student_id = e.student_id
    WHERE e.course_id = course_id_param
    ORDER BY e.enrollment_date;
END //

CREATE PROCEDURE MakePayment(
    IN student_id_param INT,
    IN amount_param DECIMAL(10,2),
    OUT payment_id_param INT
)
BEGIN
    IF amount_param <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Payment amount must be positive';
    END IF;
    
    INSERT INTO Payments (student_id, amount, payment_date)
    VALUES (student_id_param, amount_param, CURDATE());
    
    SET payment_id_param = LAST_INSERT_ID();
END //
DELIMITER ;