-- CREATING DATABASE
CREATE DATABASE airport_db;

-- USING DATABASE
USE airport_db;



-- CREATING TABLES
CREATE TABLE plane_arrivals (
	plane_id INT PRIMARY KEY AUTO_INCREMENT,
    flight VARCHAR(255) NOT NULL,
    coming_from VARCHAR(255),
    airport_code VARCHAR(255),
    airline VARCHAR(255),
    aircraft VARCHAR(255),
    landed DATETIME UNIQUE,
    on_time BOOLEAN
);

CREATE TABLE plane_departures (
	plane_id INT PRIMARY KEY AUTO_INCREMENT,
    flight VARCHAR(255) NOT NULL,
    going_to VARCHAR(255),
    airport_code VARCHAR(255),
    airline VARCHAR(255),
    aircraft VARCHAR(255),
    departed DATETIME UNIQUE,
    on_time BOOLEAN
);



-- INSERTING DATA INTO TABLES

INSERT INTO plane_arrivals (flight, coming_from, airport_code, airline, aircraft, landed, on_time)
VALUES  ("LH2472", "Munich", "MUC", "Lufthansa", "A20N", "2026-03-28 09:27:00", True),
		("EI162", "Dublin", "DUB", "Aer Lingus", "A21N", "2026-03-28 11:56:00", False),
        ("UA923", "Los Angeles", "LAX", "United Airlines", "B78X", "2026-03-28 09:35:00", True),
        ("BA296", "Chicago", "ORD", "British Airways", "B772", "2026-03-28 12:26:00", False),
        ("VS118", "Miami", "MIA", "Virgin Atlantic", "B789", "2026-03-28 12:06", True),
        ("FI450", "Reykjavik", "KEF", "Icelandair", "A21N", "2026-03-28 12:02:00", True),
        ("WS2", "Calgary", "YYC", "WestJet", "B789", "2026-03-28 11:40:00", True),
        ("SK531", "Stockholm", "ARN", "SAS", "A20N", "2026-03-28 14:56:00", False);

SELECT * FROM plane_arrivals;


INSERT INTO plane_departures (flight, going_to, airport_code, airline, aircraft, departed, on_time)
VALUES	("UA879", "Houston", "IAH", "United Airlines", "B772", "2026-03-28 10:17:00", True),
		("BA396", "Cairo", "CAI", "British Airways", "A20N", "2026-03-28 10:37:00", True),
        ("AY1332", "Helsinki", "HEL", "Finnair", "A359", "2026-03-28 10:40:00", False),
        ("AA101", "New York", "JFK", "American Airlines", "B77W", "2026-03-28 10:41:00", False),
        ("AZ203", "Rome", "FCO", "ITA Airways", "A20N", "2026-03-28 10:47:00", False),
        ("VS302", "Delhi", "DEL", "Virgin Atlantic", "A35K", "2026-03-28 10:51:00", False),
        ("KM101", "Malta", "MLA", "KM Malta Airlines", "A20N", "2026-03-28 11:05:00", True),
        ("DL51", "Salt Lake City", "SLC", "Delta Air Lines", "A332", "2026-03-28 11:16:00", False);

SELECT * FROM plane_departures;
