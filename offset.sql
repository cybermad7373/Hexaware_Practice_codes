-- Page 1 of movies (records 1-5)
SELECT * FROM Movie LIMIT 5 OFFSET 0;

-- Page 2 of movies (records 6-10)
SELECT * FROM Movie LIMIT 5 OFFSET 5;

-- Page 3 of users (records 21-30)
SELECT * FROM User LIMIT 10 OFFSET 20;

-- First 5 highest rated movies
SELECT * FROM Movie ORDER BY rating DESC LIMIT 5;

-- Next 5 highest rated movies
SELECT * FROM Movie ORDER BY rating DESC LIMIT 5 OFFSET 5;

-- First 3 most recent bookings
SELECT * FROM Booking ORDER BY booking_datetime DESC LIMIT 3;

-- First 5 available seats for show_id 1
SELECT * FROM ShowSeat 
WHERE show_id = 1 AND is_available = TRUE 
LIMIT 5;

-- Next 5 available seats for show_id 1
SELECT * FROM ShowSeat 
WHERE show_id = 1 AND is_available = TRUE 
LIMIT 5 OFFSET 5;

-- First 3 action movies
SELECT * FROM Movie 
WHERE genre = 'Action' 
LIMIT 3;

-- Page 1: First 10 food items
SELECT * FROM FoodItem LIMIT 10 OFFSET 0;

-- Page 2: Next 10 food items
SELECT * FROM FoodItem LIMIT 10 OFFSET 10;

-- Page 3: Next 10 food items
SELECT * FROM FoodItem LIMIT 10 OFFSET 20;


/*
-- Set page number and size
SET @page_number = 2;
SET @page_size = 5;

-- Dynamic pagination query
SELECT * FROM Screen 
LIMIT @page_size
OFFSET (@page_number - 1) * @page_size;
*/
