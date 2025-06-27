# Crime Management System - Database Project


# CHeck for output of the Queries [click here](https://github.com/cybermad7373/Hexaware_Practice_codes/wiki/SQL-Coding-challenge-Output)


##  Overview
This project is a basic relational database designed to manage and organize criminal case data. It includes tables for crimes, victims, and suspects, with appropriate relationships between them.

##  Tables Description

### 1. `Crime` Table
Stores details about each reported crime.

- `CrimeID` (Primary Key): Unique identifier for each crime.
- `IncidentType`: Type of incident (e.g., Robbery, Assault).
- `IncidentDate`: Date the incident occurred.
- `Location`: Place of the incident.
- `Description`: Additional details.
- `Status`: Case status (e.g., Open, Closed).

### 2. `Victim` Table
Stores information about victims linked to a crime.

- `VictimID` (Primary Key): Unique identifier for each victim.
- `CrimeID` (Foreign Key): References `Crime(CrimeID)`.
- `Name`: Victim's name.
- `ContactInfo`: Contact details.
- `Injuries`: Description of injuries, if any.

### 3. `Suspect` Table
Stores information about suspects related to a crime.

- `SuspectID` (Primary Key): Unique identifier for each suspect.
- `CrimeID` (Foreign Key): References `Crime(CrimeID)`.
- `Name`: Suspect's name.
- `Description`: Description of the suspect.
- `CriminalHistory`: Summary of past criminal records.

##  Technical Notes

- Designed for any SQL-compatible RDBMS (e.g., MySQL, PostgreSQL).
- Uses primary and foreign key constraints to maintain data relationships.
- Demonstrates basic concepts of relational database design.

##  Purpose

This project is intended for academic practice and demonstrates:
- How to model a real-world scenario using relational databases.
- Use of foreign keys for data linking.
- Simple SQL table creation and data structuring.
