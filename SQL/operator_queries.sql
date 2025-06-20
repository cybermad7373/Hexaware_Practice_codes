-- Arithmetic Operators (+, -, *, /, %)
Select total_cost, total_cost + 50 AS increased_cost FROM Booking LIMIT 3;
SELECT capacity, capacity - 10 AS reduced_capacity FROM Screen LIMIT 3;
SELECT rating, rating * 1.1 AS boosted_rating FROM Movie LIMIT 3;

-- Comparison Operators (=, !=, >, <, >=, <=)
SELECT title FROM Movie WHERE rating >= 8.0 LIMIT 3;
SELECT name FROM Screen WHERE capacity != 200 LIMIT 3;
SELECT booking_id FROM Booking WHERE total_cost < 400 LIMIT 3;

-- Logical Operators (AND, OR, NOT)
SELECT title FROM Movie WHERE rating > 7.5 AND status = 'Now Showing' LIMIT 3;
select name FROM User WHERE name LIKE 'K%' OR email LIKE '%@gmail.com' LIMIT 3;
SELECT show_id FROM Showw WHERE NOT screen_id = 1 LIMIT 3;

-- CONCAT Operator
SELECT CONCAT(title, ' (', genre, ')') AS movie_info FROM Movie LIMIT 3;
SELECT CONCAT(name, ' - ', class_type) AS screen_info FROM Screen LIMIT 3;
SELECT CONCAT('Booking #', booking_id, ' - ₹', total_cost) AS booking_summary FROM Booking LIMIT 3;

-- Wildcard Operators (% and _)
SELECT title FROM Movie WHERE title LIKE 'A%' LIMIT 3; -- Starts with A
SELECT email FROM User WHERE email LIKE '%@gmail.___' LIMIT 3; -- gmail with 3-letter 
SELECT seat_number FROM Seat WHERE seat_number LIKE 'A_' LIMIT 3; -- A followed by

-- Combined Operators
SELECT title FROM Movie WHERE rating > 7.5 AND (genre = 'Action' OR genre = 'Drama') LIMIT 3;
Select name FROM Screen WHERE capacity BETWEEN 150 AND 200 AND class_type != 'Iron' LIMIT 3;
SELECT booking_id FROM Booking WHERE total_cost > 300 AND booking_datetime < '2023-12-31' LIMIT 3;

-- Using & 
SELECT screen_id FROM Screen WHERE screen_id & 1 = 1 LIMIT 3; -- Odd numbered 
Select movie_id FROM Movie WHERE movie_id & 3 = 0 LIMIT 3; -- divisible by 4
SELECT booking_id FROM Booking WHERE booking_id & 1 = 0 LIMIT 3; -- Even numbered

-- Using _ 
Select seat_number FROM Seat WHERE seat_number LIKE '_1' LIMIT 3; -- Any row column 1
SELECT email FROM User WHERE email LIKE 'k___r@%' LIMIT 3; -- 5 letter usernames starting with k and ending with r
SELECT title FROM Movie WHERE title LIKE 'A_____n' LIMIT 3; -- 7 letter titles starting with A and ending with n