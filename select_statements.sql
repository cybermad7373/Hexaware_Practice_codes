-- Simple SELECT all columns
SELECT * FROM Movie;
SELECT * FROM Screen;
SELECT * FROM User;

-- SELECT specific columns
SELECT title, rating FROM Movie;
SELECT name, capacity FROM Screen;
SELECT name, email FROM User;

-- SELECT with WHERE clause
SELECT title, rating FROM Movie WHERE rating > 8;
SELECT name FROM Screen WHERE class_type = 'Gold';
SELECT booking_id, total_cost FROM Booking WHERE total_cost > 300;

-- SELECT with ORDER BY
SELECT title, rating FROM Movie ORDER BY rating DESC;
SELECT name, capacity FROM Screen ORDER BY capacity;
SELECT name FROM User ORDER BY name;

-- SELECT with LIMIT
SELECT title, rating FROM Movie ORDER BY rating DESC LIMIT 3;
SELECT name FROM Screen ORDER BY RAND() LIMIT 2;
SELECT name FROM User LIMIT 5;

-- SELECT with DISTINCT
SELECT DISTINCT genre FROM Movie;
SELECT DISTINCT class_type FROM Screen;
SELECT DISTINCT total_cost FROM Booking;

-- SELECT with column aliases
SELECT title AS movie_title, rating AS movie_rating FROM Movie;
SELECT name AS screen_name, capacity AS seating_capacity FROM Screen;
SELECT booking_id, total_cost AS amount_paid FROM Booking;

-- SELECT with arithmetic operations
SELECT booking_id, total_cost, total_cost * 0.1 AS tax FROM Booking;
SELECT name, capacity, capacity * 0.8 AS eighty_percent_capacity FROM Screen;
SELECT title, rating, rating * 2 AS doubled_rating FROM Movie;

-- SELECT with LIKE for pattern matching
SELECT title FROM Movie WHERE title LIKE 'A%';
SELECT name, email FROM User WHERE email LIKE '%@gmail.com';
SELECT name FROM Screen WHERE name LIKE '%e%';

-- SELECT with BETWEEN
SELECT title, rating FROM Movie WHERE rating BETWEEN 7 AND 8;
SELECT booking_id, total_cost FROM Booking WHERE total_cost BETWEEN 200 AND 400;
SELECT name, capacity FROM Screen WHERE capacity BETWEEN 150 AND 200;

-- SELECT with IN
SELECT title FROM Movie WHERE movie_id IN (1, 3, 5);
SELECT name FROM Screen WHERE name IN ('Elite', 'Premier');
SELECT booking_id FROM Booking WHERE total_cost IN (300, 450, 600);

-- SELECT with IS NULL/IS NOT NULL
SELECT title FROM Movie WHERE poster_image_url IS NULL;
SELECT name FROM User WHERE phone IS NULL;
SELECT payment_id FROM Payment WHERE failure_reason IS NOT NULL;