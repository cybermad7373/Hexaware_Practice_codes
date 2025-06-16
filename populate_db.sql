USE unox;

-- Insert screens 
INSERT INTO Screen (name, class_type, capacity) VALUES
('Elite', 'Gold', 150),
('Premier', 'Silver', 200),
('Royal', 'Gold', 180),
('Star', 'Iron', 250);

-- Insert Tamil movies 
INSERT INTO Movie (title, genre, rating, status, poster_image_url) VALUES
('Ghajini', 'Action', 8.2, 'Now Showing', 'https://example.com/ghajini.jpg'),
('Anniyan', 'Psychological Thriller', 8.4, 'Now Showing', 'https://example.com/anniyan.jpg'),
('Sivaji', 'Action', 8.1, 'Now Showing', 'https://example.com/sivaji.jpg'),
('Kanchivaram', 'Drama', 8.7, 'Now Showing', 'https://example.com/kanchivaram.jpg'),
('Kaakha Kaakha', 'Action', 8.0, 'Now Showing', 'https://example.com/kaakha-kaakha.jpg'),
('Veyil', 'Drama', 8.3, 'Now Showing', 'https://example.com/veyil.jpg'),
('Subramaniapuram', 'Gangster', 8.5, 'Now Showing', 'https://example.com/subramaniapuram.jpg');

-- Insert seats for each screen 
-- Screen 1
INSERT INTO Seat (screen_id, seat_number) VALUES
(1, 'A1'), (1, 'A2'), (1, 'A3'), (1, 'A4'), (1, 'A5'),
(1, 'B1'), (1, 'B2'), (1, 'B3'), (1, 'B4'), (1, 'B5');

-- Screen 2 
INSERT INTO Seat (screen_id, seat_number) VALUES
(2, 'A1'), (2, 'A2'), (2, 'A3'), (2, 'A4'), (2, 'A5'),
(2, 'B1'), (2, 'B2'), (2, 'B3'), (2, 'B4'), (2, 'B5');

-- Screen 3 
INSERT INTO Seat (screen_id, seat_number) VALUES
(3, 'A1'), (3, 'A2'), (3, 'A3'), (3, 'A4'), (3, 'A5'),
(3, 'B1'), (3, 'B2'), (3, 'B3'), (3, 'B4'), (3, 'B5');

-- Screen 4
INSERT INTO Seat (screen_id, seat_number) VALUES
(4, 'A1'), (4, 'A2'), (4, 'A3'), (4, 'A4'), (4, 'A5'),
(4, 'B1'), (4, 'B2'), (4, 'B3'), (4, 'B4'), (4, 'B5');

-- Insert movie casts
INSERT INTO MovieCast (movie_id, person_name, role) VALUES
(1, 'Suriya', 'Sanjay Ramaswamy'),
(1, 'Asin', 'Kalpana'),
(2, 'Vikram', 'Ambi/Remyakrishna/Anniyan'),
(2, 'Sada', 'Nandini'),
(3, 'Rajinikanth', 'Sivaji'),
(3, 'Shriya Saran', 'Tamizhselvi'),
(4, 'Prakash Raj', 'Vengadam'),
(5, 'Suriya', 'Anbuselvan'),
(5, 'Jyothika', 'Maya'),
(6, 'Pasupathy', 'Murugesan'),
(6, 'Bhavana', 'Angamma'),
(7, 'Jai', 'Azghar'),
(7, 'Sasikumar', 'Paraman');

-- Insert movie reviews (
INSERT INTO Review (movie_id, content, review_date, reviewer_name) VALUES
(1, 'Suriya''s breakthrough performance. Amazing action sequences!', '2005-10-15 14:30:00', 'Ramesh'),
(2, 'Vikram''s triple role was phenomenal. Great social message too.', '2005-06-20 09:15:00', 'Malathi'),
(3, 'Rajini''s grand comeback. Shankar''s direction at its best.', '2007-06-15 18:45:00', 'Karthik'),
(4, 'Prakash Raj''s career best performance. Moving story about weavers.', '2008-12-05 20:00:00', 'Priya'),
(5, 'Gautam Menon''s stylish cop story. Suriya-Jyothika chemistry worked well.', '2003-08-22 11:20:00', 'Suresh');

-- Insert shows for movies 
INSERT INTO Showw (screen_id, movie_id, show_datetime) VALUES
(1, 1, '2023-04-01 10:00:00'),
(2, 2, '2023-04-01 11:30:00'),
(3, 3, '2023-04-01 18:00:00'),
(4, 4, '2023-04-01 20:30:00'),
(1, 5, '2023-04-02 10:00:00'),
(2, 6, '2023-04-02 13:30:00'),
(3, 7, '2023-04-02 16:00:00');

-- Insert users
INSERT INTO User (name, email, phone) VALUES
('Rajesh', 'rajesh@example.com', '9876543210'),
('Meena', 'meena@example.com', '8765432109'),
('Karthik', 'karthik@example.com', '7654321098'),
('Priyanka', 'priyanka@example.com', NULL),
('Murali', 'murali@example.com', '6543210987');

-- Insert memberships
INSERT INTO Membership (user_id, current_points) VALUES
(1, 150),
(2, 75),
(3, 200),
(5, 50);

-- Insert show seats
INSERT INTO ShowSeat (show_id, seat_id, is_available) VALUES
(1, 1, FALSE), (1, 2, TRUE), (1, 3, TRUE), (1, 4, FALSE), (1, 5, TRUE),
(2, 1, TRUE), (2, 2, TRUE), (2, 3, FALSE), (2, 4, TRUE), (2, 5, TRUE),
(3, 11, FALSE), (3, 12, FALSE), (3, 13, TRUE), (3, 14, TRUE), (3, 15, TRUE);

-- Insert bookings
INSERT INTO Booking (user_id, show_id, booking_datetime, total_cost) VALUES
(1, 1, '2023-03-30 15:30:00', 600.00),
(2, 3, '2023-03-31 10:15:00', 450.00),
(3, 5, '2023-03-29 20:45:00', 900.00),
(5, 2, '2023-03-30 18:20:00', 300.00);

-- Insert payment gateways
INSERT INTO PaymentGateway (name) VALUES
('Banking'), ('Credit Card'), ('Paytm'), ('UPI');

-- Insert payments
INSERT INTO Payment (booking_id, gateway_id, transaction_amount, transaction_datetime, status, credit_card_name, credit_card_number, expiry_date, cvv) VALUES
(1, 2, 600.00, '2023-03-30 15:31:00', 'Completed', 'Rajesh', '1234567812345678', '2025-12-01', '123'),
(2, 4, 450.00, '2023-03-31 10:16:00', 'Completed', NULL, NULL, NULL, NULL),
(3, 1, 900.00, '2023-03-29 20:46:00', 'Completed', 'Karthik', '8765432187654321', '2024-10-01', '456'),
(4, 3, 300.00, '2023-03-30 18:21:00', 'Failed', NULL, NULL, NULL, NULL);

-- Update failed payment with reason
UPDATE Payment SET failure_reason = 'Insufficient funds' WHERE payment_id = 4;

-- Insert tickets 
INSERT INTO Ticket (booking_id, show_seat_id, qr_code, delivery_method, is_downloaded, scanned_at) VALUES
(1, 1, 'QR123456', 'WhatsApp', TRUE, '2023-04-01 09:45:00'),
(1, 4, 'QR123457', 'WhatsApp', TRUE, NULL),
(2, 11, 'QR123458', 'App', FALSE, NULL),
(2, 12, 'QR123459', 'App', FALSE, NULL),
(3, 3, 'QR123460', 'WhatsApp', TRUE, '2023-04-01 13:30:00');

-- Insert food items
INSERT INTO FoodItem (name, description, is_combo) VALUES
('Sambar Rice', 'Tasty traditional Tamil sambar rice', FALSE),
('Rasam', 'Delicious traditional rasam', FALSE),
('Parotta Kurma', 'Parotta with kurma sauce', FALSE),
('Noodles', 'Chinese noodles', FALSE),
('Cinema Combo', 'Popcorn, soda and chocolate', TRUE);

-- Insert food item sizes
INSERT INTO FoodItemSize (item_id, size_name, rate) VALUES
(1, 'Small', 80.00),
(1, 'Large', 120.00),
(2, 'Small', 40.00),
(2, 'Large', 70.00),
(3, 'Double', 90.00),
(4, 'Small', 60.00),
(4, 'Large', 100.00),
(5, 'Single', 200.00);

-- Insert food orders
INSERT INTO FoodOrder (booking_id, screen_id, seat_id, order_datetime, total_cost, delivery_method) VALUES
(1, 1, 1, '2023-04-01 09:30:00', 340.00, 'QR'),
(2, 2, 11, '2023-04-01 11:00:00', 200.00, 'Manual'),
(3, 4, 21, '2023-04-01 19:45:00', 160.00, 'QR');

-- Insert food order items
INSERT INTO FoodOrderItem (order_id, item_id, size_id, quantity, price_at_time) VALUES
(1, 5, 8, 1, 200.00),
(1, 2, 4, 2, 140.00),
(2, 5, 8, 1, 200.00),
(3, 1, 2, 1, 120.00),
(3, 2, 3, 1, 40.00);

-- Insert points transactions
INSERT INTO PointsTransaction (user_id, amount, points_earned, transaction_datetime, transaction_type) VALUES
(1, 600.00, 60, '2023-03-30 15:31:00', 'Booking'),
(2, 450.00, 45, '2023-03-31 10:16:00', 'Booking'),
(3, 900.00, 90, '2023-03-29 20:46:00', 'Booking'),
(5, 300.00, 30, '2023-03-30 18:21:00', 'Booking'),
(1, 340.00, 34, '2023-04-01 09:30:00', 'Food'),
(2, 200.00, 20, '2023-04-01 11:00:00', 'Food');