-- DATE/TIME EXTRACTION
SELECT show_id, show_datetime, YEAR(show_datetime) AS show_year FROM Showw LIMIT 3;
SELECT booking_datetime, MONTHNAME(booking_datetime) AS booking_month FROM Booking LIMIT 3;
SELECT review_date, DAYOFWEEK(review_date) AS day_of_week FROM Review LIMIT 3;

-- DATE FORMATTING
SELECT show_datetime, DATE_FORMAT(show_datetime, '%W, %M %e %Y') AS formatted_date FROM Showw LIMIT 3;
SELECT booking_datetime, DATE_FORMAT(booking_datetime, '%l:%i %p') AS formatted_time FROM Booking LIMIT 3;
SELECT review_date, DATE_FORMAT(review_date, '%b %d, %Y') AS short_date FROM Review LIMIT 3;

-- DATE ARITHMETIC
SELECT show_datetime, DATE_ADD(show_datetime, INTERVAL 1 DAY) AS next_day FROM Showw LIMIT 3;
SELECT booking_datetime, DATE_SUB(booking_datetime, INTERVAL 2 HOUR) AS two_hours_earlier FROM Booking LIMIT 3;
SELECT review_date, review_date + INTERVAL 1 WEEK AS next_week FROM Review LIMIT 3;

-- DATE COMPARISON
SELECT title, show_datetime FROM Showw WHERE show_datetime > NOW() LIMIT 3;
Select booking_id, booking_datetime FROM Booking WHERE booking_datetime < '2023-12-31' LIMIT 3;
SELECT review_id, review_date FROM Review WHERE review_date BETWEEN '2023-01-01' AND '2023-12-31' LIMIT 3;

-- TIME DIFFERENCES
SELECT show_id, TIMESTAMPDIFF(HOUR, NOW(), show_datetime) AS hours_remaining FROM Showw LIMIT 3;
SELECT booking_id, DATEDIFF(NOW(), booking_datetime) AS days_since_booking FROM Booking LIMIT 3;
SELECT review_id, TIMESTAMPDIFF(DAY, review_date, NOW()) AS days_old FROM Review LIMIT 3;

-- DATE AGGREGATION
Select DATE(show_datetime) AS show_date, COUNT(*) AS shows_per_day FROM Showw GROUP BY show_date LIMIT 3;
SELECT MONTH(booking_datetime) AS month, SUM(total_cost) AS monthly_revenue FROM Booking GROUP BY month LIMIT 3;
SELECT HOUR(show_datetime) AS hour_of_day, COUNT(*) AS shows_count FROM Showw GROUP BY hour_of_day LIMIT 3;

-- SPECIAL DATE FUNCTIONS
SELECT LAST_DAY(show_datetime) AS month_end FROM Showw LIMIT 3;
SELECT booking_datetime, WEEKOFYEAR(booking_datetime) AS week_number FROM Booking LIMIT 3;
SELECT review_date, QUARTER(review_date) AS quarter FROM Review LIMIT 3;

-- TIMEZONE CONVERSION
SELECT show_datetime, CONVERT_TZ(show_datetime, '+00:00', '+05:30') AS ist_time FROM Showw LIMIT 3;
SELECT booking_datetime, CONVERT_TZ(booking_datetime, @@session.time_zone, 'UTC') AS utc_timee FROM Booking LIMIT 3;
SELECT review_date, CONVERT_TZ(review_date, 'SYSTEM', 'America/New_York') AS ny_time FROM Review LIMIT 3;

-- DATE VALIDATION
Select show_datetime, ISDATE(show_datetime) AS is_valid_date FROM Showw LIMIT 3;
SELECT booking_datetime, DAYNAME(booking_datetime) AS day_name FROM Booking WHERE DAYOFWEEK(booking_datetime) = 1 LIMIT 3;
SELECT review_date, CASE WHEN review_date > NOW() THEN 'Future' ELSE 'Past' END AS time_status FROM Review LIMIT 3;