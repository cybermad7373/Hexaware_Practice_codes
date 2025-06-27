-- Add age column to Victim table
ALTER TABLE Victim ADD COLUMN Age INT;

-- Add age column to Suspect table
ALTER TABLE Suspect ADD COLUMN Age INT;

-- Update Victim ages
UPDATE Victim SET Age = 45 WHERE VictimID = 1; 
UPDATE Victim SET Age = 32 WHERE VictimID = 2;  
UPDATE Victim SET Age = 28 WHERE VictimID = 3; 

-- Update Suspect ages
UPDATE Suspect SET Age = 30 WHERE SuspectID = 1;  
UPDATE Suspect SET Age = NULL WHERE SuspectID = 2;  
UPDATE Suspect SET Age = 35 WHERE SuspectID = 3; 

-- Add more data 
INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status)
VALUES
(4, 'Assault', '2023-09-05', '321 Pine St, Cityville', 'Bar fight resulting in injuries', 'Open'),
(5, 'Robbery', '2023-09-18', '654 Maple St, Townsville', 'Bank robbery', 'Under Investigation');

INSERT INTO Victim (VictimID, CrimeID, Name, ContactInfo, Injuries, Age)
VALUES
(4, 4, 'Bob Brown', 'bobbrown@example.com', 'Broken nose', 30),
(5, 5, 'Sarah Connor', 'sarahc@example.com', 'None', 35);

INSERT INTO Suspect (SuspectID, CrimeID, Name, Description, CriminalHistory, Age)
VALUES
(4, 4, 'Mike Tyson', 'Known boxer', 'Prior assault charges', 35),
(5, 5, 'John Dillinger', 'Bank robber', 'Multiple robbery convictions', 40),
(6, 1, 'Jane Doe', 'Accomplice', 'Petty theft', 25);  