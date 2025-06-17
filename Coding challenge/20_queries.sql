-- 1. select all open incidents.
select *
from Crime
where Status = 'Open';

-- ------------------------------------------------------------------------------------------------------------
-- 2. Find the total number of incidents.
select COUNT(*) as TotalIncidents from Crime;

-- ------------------------------------------------------------------------------------------------------------
-- 3. List all unique incident types.
select DISTINCT IncidentType from Crime;

-- ------------------------------------------------------------------------------------------------------------
-- 4. Retrieve incidents that occurred between '2023-09-01' and '2023-09-10'.
select * from Crime 
where IncidentDate between '2023-09-01' and '2023-09-10';

-- ------------------------------------------------------------------------------------------------------------
-- 5. List persons involved in incidents in descending order of age.
(select 'Victim' as Role, Name, Age, CrimeID from Victim where Age IS NOT NULL)
UNION ALL
(select 'Suspect' as Role, Name, Age, CrimeID from Suspect where Age IS NOT NULL)
ORDER BY Age DESC;

-- ------------------------------------------------------------------------------------------------------------
-- 6. Find the average age of persons involved in incidents.
select AVG(Age) as AverageAge
from (
    select Age from Victim where Age IS NOT NULL
    UNION ALL
    select Age from Suspect where Age IS NOT NULL
) as AllAges;

-- ------------------------------------------------------------------------------------------------------------
-- 7. List incident types and their counts, only for open cases.
select IncidentType, COUNT(*) as Count 
from Crime 
where Status = 'Open' 
GROUP BY IncidentType;

-- ------------------------------------------------------------------------------------------------------------
-- 8. Find persons with names containing 'Doe'.
-- Victims
select * from Victim 
where Name LIKE '%Doe%';
-- Suspects
select * from Suspect 
where Name LIKE '%Doe%';

-- ------------------------------------------------------------------------------------------------------------
-- 9. Retrieve the names of persons involved in open cases and closed cases.
-- Victims
select v.Name, c.Status 
from Victim v JOIN Crime c 
ON v.CrimeID = c.CrimeID;
-- Suspects
select s.Name, c.Status 
from Suspect s JOIN Crime c 
ON s.CrimeID = c.CrimeID;

-- ------------------------------------------------------------------------------------------------------------
-- 10. List incident types where there are persons aged 30 or 35 involved.
select DISTINCT c.IncidentType
from Crime c
JOIN (
    select CrimeID from Victim where Age IN (30, 35)
    UNION
    select CrimeID from Suspect where Age IN (30, 35)
) as Persons 
ON c.CrimeID = Persons.CrimeID;

-- ------------------------------------------------------------------------------------------------------------
-- 11. Find persons involved in incidents of the same type as 'Robbery'.
-- Victims
select v.* 
from Victim v JOIN Crime c 
ON v.CrimeID = c.CrimeID 
where c.IncidentType = 'Robbery';
-- Suspects
select s.* 
from Suspect s JOIN Crime c 
ON s.CrimeID = c.CrimeID 
where c.IncidentType = 'Robbery';

-- ------------------------------------------------------------------------------------------------------------
-- 12. List incident types with more than one open case.
select IncidentType, COUNT(*) as OpenCases
from Crime
where Status = 'Open'
GROUP BY IncidentType
HAVING COUNT(*) > 1;

-- ------------------------------------------------------------------------------------------------------------
-- 13. List all incidents with suspects whose names also appear as victims in other incidents.
select c.* 
from Crime c
JOIN Suspect s 
ON c.CrimeID = s.CrimeID
where s.Name IN (select Name from Victim);

-- ------------------------------------------------------------------------------------------------------------
-- 14. Retrieve all incidents along with victim and suspect details.
select c.*, v.Name as VictimName, v.ContactInfo, v.Injuries, 
       s.Name as SuspectName, s.Description as SuspectDesc, s.CriminalHistory
from Crime c
LEFT JOIN Victim v 
ON c.CrimeID = v.CrimeID
LEFT JOIN Suspect s 
ON c.CrimeID = s.CrimeID;

-- ------------------------------------------------------------------------------------------------------------
-- 15. Find incidents where the suspect is older than any victim.
select DISTINCT c.*
from Crime c
JOIN Suspect s 
ON c.CrimeID = s.CrimeID
JOIN Victim v 
ON c.CrimeID = v.CrimeID
where s.Age > v.Age;

-- ------------------------------------------------------------------------------------------------------------
-- 16. Find suspects involved in multiple incidents:
select s.Name, COUNT(*) as IncidentCount
from Suspect s
GROUP BY s.Name
HAVING COUNT(*) > 1;

-- ------------------------------------------------------------------------------------------------------------
-- 17. List incidents with no suspects involved.
select c.*
from Crime c
LEFT JOIN Suspect s 
ON c.CrimeID = s.CrimeID
where s.SuspectID IS NULL;

-- ------------------------------------------------------------------------------------------------------------
-- 18. List all cases where at least one incident is of type 'Homicide' and all other incidents are of type
-- 'Robbery'.
select DISTINCT c1.*
from Crime c1
where EXISTS (
    select 1 from Crime c2 
    where c2.IncidentType = 'Homicide'
)
AND NOT EXISTS (
    select 1 from Crime c3 
    where c3.IncidentType NOT IN ('Homicide', 'Robbery')
);

-- ------------------------------------------------------------------------------------------------------------
-- 19. Retrieve a list of all incidents and the associated suspects, showing suspects for each incident, or
-- 'No Suspect' if there are none.
select c.*, COALESCE(s.Name, 'No Suspect') as SuspectName
from Crime c
LEFT JOIN Suspect s
 ON c.CrimeID = s.CrimeID;

-- ------------------------------------------------------------------------------------------------------------
-- 20. List all suspects who have been involved in incidents with incident types 'Robbery' or 'assault'
select DISTINCT s.*
from Suspect s
JOIN Crime c 
ON s.CrimeID = c.CrimeID
where c.IncidentType IN ('Robbery', 'assault');