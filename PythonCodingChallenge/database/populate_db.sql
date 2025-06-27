-- Use the database
USE loan_management_system;

-- Insert sample customers
INSERT INTO Customer (name, email_address, phone_number, address, credit_score) VALUES
('Ruthra Kumar', 'ruthra.kumar@example.com', '9876543210', 'Chennai, Tamil Nadu', 780),
('Meena Priya', 'meena.priya@example.com', '9123456780', 'Coimbatore, Tamil Nadu', 720),
('Arun Raj', 'arun.raj@example.com', '9001234567', 'Madurai, Tamil Nadu', 690),
('Kaviya Lakshmi', 'kaviya.lakshmi@example.com', '9898989898', 'Salem, Tamil Nadu', 800),
('Vignesh Shankar', 'vignesh.shankar@example.com', '9786452310', 'Tirunelveli, Tamil Nadu', 750);

-- Insert sample loans (home and car loans)
INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status, property_address, property_value, car_model, car_value) VALUES
-- Home Loan for Ruthra
(1, 2500000.00, 7.50, 240, 'HomeLoan', 'Approved', '12, Gandhi Street, Chennai', 3000000.00, NULL, NULL),
-- Car Loan for Meena
(2, 600000.00, 8.25, 60, 'CarLoan', 'Approved', NULL, NULL, 'Hyundai i20', 650000.00),
-- Rejected Home Loan for Arun
(3, 1500000.00, 7.00, 180, 'HomeLoan', 'Rejected', '34, Lotus Nagar, Madurai', 1800000.00, NULL, NULL),
-- Pending Car Loan for Kaviya
(4, 850000.00, 9.00, 72, 'CarLoan', 'Pending', NULL, NULL, 'Maruti Suzuki Baleno', 900000.00),
-- Approved Home Loan for Vignesh
(5, 3000000.00, 7.25, 300, 'HomeLoan', 'Approved', '78, Bharathi Colony, Tirunelveli', 3500000.00, NULL, NULL);
