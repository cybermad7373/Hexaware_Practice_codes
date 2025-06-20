-- Create database
CREATE DATABASE IF NOT EXISTS CinemaDB;
USE CinemaDB;

-- Create sample table
CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(50),
    Rating DECIMAL(3,1)
);

-- Create user
CREATE USER 'CinemaStaff'@'localhost' IDENTIFIED BY 'SecureCine@123';

-- Basic permissions
GRANT SELECT, INSERT, UPDATE ON CinemaDB.Movies TO 'CinemaStaff'@'localhost';

-- Procedure permission
GRANT EXECUTE ON PROCEDURE CinemaDB.sp_AddMovie TO 'CinemaStaff'@'localhost';

-- Column-specific permission
GRANT UPDATE (Title, Genre) ON CinemaDB.Movies TO 'CinemaStaff'@'localhost';

-- Show grants for user
SHOW GRANTS FOR 'CinemaStaff'@'localhost';

-- Check table privileges
SELECT * FROM information_schema.table_privileges 
WHERE grantee = "'CinemaStaff'@'localhost'";

-- Remove insert privilege
REVOKE INSERT ON CinemaDB.Movies FROM 'CinemaStaff'@'localhost';

-- Remove column update
REVOKE UPDATE (Title) ON CinemaDB.Movies FROM 'CinemaStaff'@'localhost';

-- Remove procedure execution
REVOKE EXECUTE ON PROCEDURE CinemaDB.sp_AddMovie FROM 'CinemaStaff'@'localhost';

-- Simple commit
START TRANSACTION;
INSERT INTO Movies VALUES (1, 'Inception', 'Sci-Fi', 8.8);
COMMIT;

-- Rollback example
START TRANSACTION;
INSERT INTO Movies VALUES (2, 'Interstellar', 'Sci-Fi', 8.6);
ROLLBACK; 

-- Savepoint example
START TRANSACTION;
INSERT INTO Movies VALUES (3, 'The Dark Knight', 'Action', 9.0);
SAVEPOINT Point1;
INSERT INTO Movies VALUES (4, 'Pulp Fiction', 'Crime', 8.9);
ROLLBACK TO Point1;
COMMIT;

-- Remove user
DROP USER 'CinemaStaff'@'localhost';

-- Verify removal
SELECT user FROM mysql.user WHERE user = 'CinemaStaff';

-- Create role
CREATE ROLE 'MovieManagers';

-- Grant to role
GRANT SELECT, INSERT, UPDATE ON CinemaDB.Movies TO 'MovieManagers';

-- Assign role to user
GRANT 'MovieManagers' TO 'CinemaStaff'@'localhost';

-- Activate roles
SET DEFAULT ROLE 'MovieManagers' TO 'CinemaStaff'@'localhost';
