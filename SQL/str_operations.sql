-- CONCAT
SELECT CONCAT(title, ' (', genre, ')') AS movie_info FROM Movie LIMIT 3;
SELECT CONCAT(name, ' - ₹', total_cost) AS booking_summary FROM Booking b JOIN User u ON b.user_id = u.user_id LIMIT 3;
SELECT CONCAT('Screen ', name, ' (', class_type, ')') AS screen_details FROM Screen LIMIT 3;

-- LENGTH
SELECT title, LENGTH(title) AS title_length FROM Movie LIMIT 3;
SELECT name, LENGTH(name) AS name_length FROM User WHERE LENGTH(name) > 10 LIMIT 3;
SELECT seat_number, LENGTH(seat_number) AS seat_num_length FROM Seat LIMIT 3;

-- TRIM
SELECT TRIM(title) AS trimmed_title FROM Movie LIMIT 3;
SELECT LTRIM(seat_number) AS left_trimmed FROM Seat LIMIT 3;
SELECT RTRIM(name) AS right_trimmed FROM Screen LIMIT 3;

-- SUBSTRING 
SELECT title, SUBSTRING(title, 1, 5) AS short_title FROM Movie LIMIT 3;
SELECT seat_number, SUBSTRING(seat_number, 2) AS seat_row FROM Seat LIMIT 3;
SELECT email, SUBSTRING_INDEX(email, '@', 1) AS username FROM User LIMIT 3;

-- LIKE
SELECT title FROM Movie WHERE title LIKE '%the%' LIMIT 3;
SELECT name FROM User WHERE name LIKE 'A%' LIMIT 3;
SELECT seat_number FROM Seat WHERE seat_number LIKE '_1' LIMIT 3;

-- REPLACE
SELECT title, REPLACE(title, ' ', '-') AS hyphenated_title FROM Movie LIMIT 3;
SELECT name, REPLACE(name, 'Mr.', '') AS clean_name FROM User LIMIT 3;
SELECT class_type, REPLACE(class_type, 'Gold', 'Premium') AS updated_class FROM Screen LIMIT 3;

-- LOCATE
SELECT title, LOCATE(' ', title) AS first_space_pos FROM Movie LIMIT 3;
SELECT email, LOCATE('@', email) AS at_position FROM User LIMIT 3;
SELECT seat_number, LOCATE('1', seat_number) AS one_position FROM Seat LIMIT 3;

-- FORMAT
SELECT title, FORMAT(rating, 1) AS formatted_rating FROM Movie LIMIT 3;
SELECT total_cost, CONCAT('₹', FORMAT(total_cost, 2)) AS formatted_cost FROM Booking LIMIT 3;
SELECT capacity, FORMAT(capacity, 0) AS formatted_capacity FROM Screen LIMIT 3;