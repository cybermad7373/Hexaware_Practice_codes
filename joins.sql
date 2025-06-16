-- Basic INNER JOIN
SELECT * FROM Movie m INNER JOIN Showw s ON m.movie_id = s.movie_id LIMIT 3;

-- INNER JOIN with specific columns
SELECT m.title, s.show_datetime, sc.name 
FROM Showw s 
INNER JOIN Movie m 
ON s.movie_id = m.movie_id 
INNER JOIN Screen sc 
ON s.screen_id = sc.screen_id 
LIMIT 3;

-- INNER JOIN with filtering
SELECT m.title, COUNT(b.booking_id) AS bookings_count
FROM Movie m
INNER JOIN Showw s 
ON m.movie_id = s.movie_id
INNER JOIN Booking b 
ON s.show_id = b.show_id
WHERE m.rating > 8.0
GROUP BY m.title
LIMIT 3;

-- Basic LEFT JOIN 
SELECT * FROM Movie m LEFT JOIN Review r 
ON m.movie_id = r.movie_id LIMIT 3;

-- LEFT JOIN with specific columns
SELECT m.title, COUNT(r.review_id) AS review_count
FROM Movie m
LEFT JOIN Review r 
ON m.movie_id = r.movie_id
GROUP BY m.title
LIMIT 3;

-- LEFT JOIN with WHERE condition
select u.name, b.booking_datetime, b.total_cost
FROM User u
LEFT JOIN Booking b 
ON u.user_id = b.user_id
WHERE b.booking_datetime > '2023-01-01'
LIMIT 3;

-- Basic RIGHT JOIN (all columns)
SELECT * FROM Booking b RIGHT JOIN User u 
ON b.user_id = u.user_id LIMIT 3;

-- RIGHT JOIN with specific columns
SELECT u.name, COUNT(b.booking_id) AS booking_count
FROM Booking b
RIGHT JOIN User u 
ON b.user_id = u.user_id
GROUP BY u.name
LIMIT 3;

-- RIGHT JOIN with filtering
SELECT sc.name, COUNT(sh.show_id) AS show_count
FROM Showw sh
RIGHT JOIN Screen sc 
ON sh.screen_id = sc.screen_id
WHERE sc.class_type = 'Gold'
GROUP BY sc.name
LIMIT 3;

-- Simulated FULL OUTER JOIN 
SELECT * FROM Movie m LEFT JOIN Review r 
ON m.movie_id = r.movie_id
UNION
Select * FROM Movie m RIGHT JOIN Review r 
ON m.movie_id = r.movie_id WHERE m.movie_id IS NULL
LIMIT 3;

-- Simulated FULL OUTER JOIN with specific columns
SELECT m.title, r.review_date, r.reviewer_name
FROM Movie m LEFT JOIN Review r 
ON m.movie_id = r.movie_id
UNION
Select m.title, r.review_date, r.reviewer_name
FROM Movie m RIGHT JOIN Review r 
ON m.movie_id = r.movie_id WHERE m.movie_id IS NULL
LIMIT 3;

-- Simulated FULL OUTER JOIN with filtering
SELECT u.name, b.booking_datetime, b.total_cost
FROM User u LEFT JOIN Booking b 
ON u.user_id = b.user_id
UNION
Select u.name, b.booking_datetime, b.total_cost
FROM User u RIGHT JOIN Booking b 
ON u.user_id = b.user_id WHERE u.user_id IS NULL
LIMIT 3;

-- Basic CROSS JOIN
SELECT * FROM Movie CROSS JOIN Screen LIMIT 3;

-- CROSS JOIN with specific columns
select m.title, s.name, s.class_type
FROM Movie m
CROSS JOIN Screen s
WHERE m.genre = 'Action'
LIMIT 3;

-- CROSS JOIN with calculation
Select m.title, s.name, (m.rating * 10) AS rating_percent, s.capacity
FROM Movie m
CROSS JOIN Screen s
ORDER BY m.rating DESC
LIMIT 3;

-- Basic SELF JOIN
SELECT * FROM User u1 JOIN User u2 
ON u1.user_id <> u2.user_id LIMIT 3;

-- SELF JOIN with specific columns
SELECT u1.name AS user1, u2.name AS user2, u1.email
FROM User u1
JOIN User u2 
ON u1.user_id < u2.user_id
LIMIT 3;

-- SELF JOIN with filtering
Select u1.name AS high_spender, u2.name AS other_user
FROM User u1
JOIN User u2 
ON u1.user_id <> u2.user_id
WHERE u1.user_id IN (SELECT user_id FROM Booking GROUP BY user_id HAVING SUM(total_cost) > 500)
LIMIT 3;