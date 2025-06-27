-- Create database
CREATE DATABASE IF NOT EXISTS loan_management_system;
USE loan_management_system;

-- Create Customer table
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email_address VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    credit_score INT NOT NULL
);

-- Create Loan table
CREATE TABLE IF NOT EXISTS Loan (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    principal_amount DECIMAL(15, 2) NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    loan_term INT NOT NULL COMMENT 'Loan Tenure in months',
    loan_type ENUM('CarLoan', 'HomeLoan') NOT NULL,
    loan_status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending',
    property_address VARCHAR(255),
    property_value DECIMAL(15, 2),
    car_model VARCHAR(100),
    car_value DECIMAL(15, 2),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);