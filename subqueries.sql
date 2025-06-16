-- Single-value subquery
SELECT title FROM Movie 
WHERE rating > (SELECT AVG(rating) FROM Movie) 
LIMIT 3;

SELECT name FROM Screen 
WHERE capacity > (SELECT AVG(capacity) FROM Screen) 
LIMIT 3;

SELECT total_cost FROM Booking 
WHERE total_cost < (SELECT AVG(total_cost) FROM Booking) 
LIMIT 3;

-- Multi-value subquery
SELECT title FROM Movie 
WHERE movie_id IN (SELECT movie_id FROM Review) 
LIMIT 3;

SELECT name FROM User 
WHERE user_id IN (SELECT user_id FROM Booking WHERE total_cost > 300) 
LIMIT 3;

SELECT seat_number FROM Seat 
WHERE screen_id IN (SELECT screen_id FROM Screen WHERE class_type = 'Gold') 
LIMIT 3;

-- Correlated subquery
SELECT m.title FROM Movie m 
WHERE EXISTS (SELECT 1 FROM Review r WHERE r.movie_id = m.movie_id) 
LIMIT 3;

SELECT s.name FROM Screen s 
WHERE EXISTS (SELECT 1 FROM Showw sh WHERE sh.screen_id = s.screen_id) 
LIMIT 3;

SELECT u.name FROM User u 
WHERE EXISTS (SELECT 1 FROM Booking b WHERE b.user_id = u.user_id) 
LIMIT 3;

-- Simple derived table
SELECT avg_rating FROM 
(SELECT genre, AVG(rating) AS avg_rating FROM Movie GROUP BY genre) AS genre_stats 
LIMIT 3;

SELECT booking_count FROM 
(SELECT user_id, COUNT(*) AS booking_count FROM Booking GROUP BY user_id) AS user_bookings 
LIMIT 3;

SELECT show_count FROM 
(SELECT screen_id, COUNT(*) AS show_count FROM Showw GROUP BY screen_id) AS screen_stats 
LIMIT 3;

-- Derived table with calculation
SELECT genre, avg_rating FROM 
(SELECT genre, AVG(rating) AS avg_rating FROM Movie GROUP BY genre) AS genre_stats 
WHERE avg_rating > 7.5 
LIMIT 3;

SELECT user_id, total_spent FROM 
(SELECT user_id, SUM(total_cost) AS total_spent FROM Booking GROUP BY user_id) AS user_spending 
WHERE total_spent > 500 
LIMIT 3;

SELECT screen_id, avg_capacity FROM 
(SELECT screen_id, AVG(capacity) AS avg_capacity FROM Screen GROUP BY screen_id) AS screen_capacity 
WHERE avg_capacity > 180 
LIMIT 3;

-- Scalar subquery in SELECT
SELECT title, (SELECT COUNT(*) FROM Review r WHERE r.movie_id = m.movie_id) AS review_count 
FROM Movie m 
LIMIT 3;

SELECT name, (SELECT COUNT(*) FROM Booking b WHERE b.user_id = u.user_id) AS booking_count 
FROM User u 
LIMIT 3;

SELECT name, (SELECT COUNT(*) FROM Showw s WHERE s.screen_id = sc.screen_id) AS show_count 
FROM Screen sc 
LIMIT 3;

-- Correlated subquery in SELECT
SELECT m.title, 
       (SELECT AVG(rating) FROM Review r WHERE r.movie_id = m.movie_id) AS avg_review_rating 
FROM Movie m 
LIMIT 3;

SELECT s.name, 
       (SELECT MAX(total_cost) FROM Booking b JOIN Showw sh ON b.show_id = sh.show_id 
        WHERE sh.screen_id = s.screen_id) AS max_booking 
FROM Screen s 
LIMIT 3;

SELECT u.name, 
       (SELECT SUM(total_cost) FROM Booking b WHERE b.user_id = u.user_id) AS total_spent 
FROM User u 
LIMIT 3;

-- Subquery in HAVING
SELECT genre, AVG(rating) 
FROM Movie 
GROUP BY genre 
HAVING AVG(rating) > (SELECT AVG(rating) FROM Movie) 
LIMIT 3;

SELECT user_id, SUM(total_cost) 
FROM Booking 
GROUP BY user_id 
HAVING SUM(total_cost) > (SELECT AVG(total_cost) FROM Booking) 
LIMIT 3;

SELECT screen_id, COUNT(*) 
FROM Showw 
GROUP BY screen_id 
HAVING COUNT(*) > (SELECT AVG(show_count) FROM 
                  (SELECT COUNT(*) AS show_count FROM Showw GROUP BY screen_id) AS counts) 
LIMIT 3;

-- ALL operator
SELECT title, rating 
FROM Movie 
WHERE rating > ALL (SELECT rating FROM Movie WHERE genre = 'Horror') 
LIMIT 3;

SELECT name, capacity 
FROM Screen 
WHERE capacity > ALL (SELECT capacity FROM Screen WHERE class_type = 'Silver') 
LIMIT 3;

SELECT booking_id, total_cost 
FROM Booking 
WHERE total_cost > ALL (SELECT total_cost FROM Booking WHERE user_id = 2) 
LIMIT 3;

-- ANY/SOME operator
SELECT title, rating 
FROM Movie 
WHERE rating > ANY (SELECT rating FROM Movie WHERE genre = 'Drama') 
LIMIT 3;

SELECT name, capacity 
FROM Screen 
WHERE capacity < ANY (SELECT capacity FROM Screen WHERE class_type = 'Gold') 
LIMIT 3;

SELECT booking_id, total_cost 
FROM Booking 
WHERE total_cost < SOME (SELECT total_cost FROM Booking WHERE user_id = 1) 
LIMIT 3;