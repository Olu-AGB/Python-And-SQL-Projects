-- For all the tables, lowercase was used and when creating the function and stored procedure, Camel Case was used.

-- CREATING DATABASE --

-- Creating Birds Database
CREATE DATABASE birds;

-- Using the Birds Database
USE birds;

-- CREATING TABLES, USING CONSTRAINTS AND NORMALISING DATA --

-- Creating Table for Species
CREATE TABLE species (
	specie_id INT PRIMARY KEY AUTO_INCREMENT,
    specie VARCHAR(255) UNIQUE,
    specie_type VARCHAR(255),
    feather_colour VARCHAR(255),
    weight_in_grams INT NOT NULL,
    wingspan_in_cm DECIMAL(5, 2) NOT NULL
);
SELECT *
FROM species;

-- Creating Table for Characteristics
CREATE TABLE characteristics (
	character_id INT PRIMARY KEY AUTO_INCREMENT,
    specie_id INT UNIQUE,
    habitat VARCHAR(255),
    diet VARCHAR(255),
    description VARCHAR(255),
    CONSTRAINT fk_character_specie
		FOREIGN KEY (specie_id)
        REFERENCES species(specie_id)
);
SELECT *
FROM characteristics;

-- Creating table for Region
/*CREATE TABLE region (
	region_id INT PRIMARY KEY AUTO_INCREMENT,
    character_id INT UNIQUE,
    country VARCHAR(255),
    continent VARCHAR(255),
    CONSTRAINT region_character
		FOREIGN KEY (character_id)
		REFERENCES characteristics(character_id)
);
SELECT *
FROM region;*/

-- The database above only achieves 2NF, so we need to split the region table as country depends on continent

-- Creating Table for Country
CREATE TABLE country (
	country_id INT PRIMARY KEY AUTO_INCREMENT,
    country VARCHAR(255),
    continent VARCHAR(255)
);

-- Recreating Table for Region
CREATE TABLE region (
	region_id INT PRIMARY KEY AUTO_INCREMENT,
    character_id INT UNIQUE,
    country_id INT,
    FOREIGN KEY (character_id)
    REFERENCES characteristics(character_id),
    FOREIGN KEY (country_id)
    REFERENCES country(country_id)
);
-- Now the tables within the database meet the conditions for Third Normal Form.


-- DEMONSTRATION FOR INSERT INTO --

-- Populating All 4 Tables
INSERT INTO species (specie, specie_type, feather_colour, weight_in_grams, wingspan_in_cm)
VALUES  ("Bald Eagle", "Bird of Prey", "Brown/White", 4500, 200.50),
		("Peregrine Falcon", "Bird of Prey", "Blue/Grey", 900, 120.75),
        ("Parrot", "Companion bird", "Green", 400, 40.25),
        ("Penguin", "Flightless Bird", "Black/White", 30000, 89),
        ("Peacock", "Game Bird", "Multicolour", 6000, 150.80),
        ("Sparrow", "Songbird", "Brown", 25, 20.10),
        ("Owl", "Bird of Prey", "Brown/White", 1500, 95.60),
        ("Flamingo", "Wading Bird", "Pink", 3500, 140.30),
        ("Albatross", "Seabird", "White/Black", 8000, 320.00),
        ("Hummingbird", "Songbird", "Green/Red", 5, 12.50);
SELECT *
FROM species
ORDER BY weight_in_grams DESC;


INSERT INTO characteristics (specie_id, habitat, diet, description)
VALUES  (1, "Forests", "Carnivore", "Strong predator with sharp vision"),
		(2, "Cliffs", "Carnivore", "Fastest bird, known for diving speed"),
        (3, "Tropical Forests", "Herbivore", "Colourful and intelligent bird"),
        (4, "Antarctic", "Carnivore", "Flightless swimmer adapted to cold"),
        (5, "Grasslands", "Omnivore", "Displays vibrant tail feathers"),
        (6, "Urban Areas", "Omnivore", "Small and commonly found near humans"),
        (7, "Woodlands", "Carnivore", "Nocturnal hunter with silent flight"),
        (8, "Wetlands", "Omnivore", "Feeds in shallow waters"),
        (9, "Oceans", "Carnivore", "Long-distance glider with large wingspan"),
        (10, "Gardens", "Herbivore", "Feeds on nectar and can hover");
SELECT *
FROM characteristics
ORDER BY diet ASC;


INSERT INTO country (country, continent)
VALUES  ("USA", "North America"),
		("UK", "Europe"),
        ("Brazil", "South America"),
        ("Antarctica", "Antarctica"),
        ("India", "Asia"),
        ("USA", "North America"),
        ("Canada", "North America"),
        ("Kenya", "Africa"),
        ("New Zealand", "Oceania"),
        ("Mexico", "North America");
SELECT *
FROM country;


INSERT INTO region (character_id, country_id)
VALUES  (1, 1),
		(2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10);
SELECT *
FROM region;


-- DEMONSTRATION ON OTHER WAYS ON RETRIEVING DATA FROM THE TABLES--

SELECT specie_type, weight_in_grams FROM species
WHERE weight_in_grams > 5000
ORDER BY weight_in_grams DESC;

SELECT specie_id, habitat, description FROM characteristics
WHERE specie_id <= 5
ORDER BY specie_id ASC;

SELECT country_id, country, continent FROM country
WHERE country_id != 10
ORDER BY country_id DESC;


-- DEMONSTRATION ON ADDING AND DELETING DATA FROM TABLE --

-- Adding Data to country table
INSERT INTO country (country, continent)
VALUES  ("Australia", "Oceania");
SELECT *
FROM country;

-- Deleting Data from region table
DELETE FROM country
WHERE country_id = 11;
SELECT *
FROM country;

-- DEMONSTRATION ON USING AGGREGATE FUNCTIONS --

SELECT SUM(weight_in_grams) -- calculating total weight across all birds in grams
FROM species;

SELECT AVG(weight_in_grams) -- calculating the average weight across all birds in grams
FROM species;

SELECT MAX(wingspan_in_cm)  -- finding the bird with the longest wingspan in cm
FROM species;

SELECT MIN(wingspan_in_cm) -- finding the bird with the shortest wingspan in cm
FROM species;


-- DEMONSTRATION ON ADDITIONAL INBUILT FUNCTIONS --

SELECT UPPER(description) AS UppercaseDescription -- shows all the rows in description in uppercase
FROM characteristics
ORDER BY description ASC;

SELECT CONCAT(country, ", ", continent) AS CountryandContinent -- shows the country with the continent concatenated together
FROM country
ORDER BY country ASC;


-- DEMONSTRATION ON JOINS --

-- Inner Join
-- Creating an inner join to join specie, specie_type and description on specie_id.
-- This join can be useful for Rsearch Scientists wanting to match the descriptions of the physical appearances of each bird specie.

SELECT species.specie, species.specie_type, characteristics.description
FROM characteristics
INNER JOIN species
ON characteristics.specie_id = species.specie_id;

-- Left Join
-- Creating a left join to join continent, country and habitat through the link table region.
-- This left join can be useful for Research Scientists for analysing the different habitats birds can live in acoss different countries and continents.

SELECT co.continent, co.country, r.character_id, ch.habitat
FROM region r
LEFT JOIN country co
ON r.country_id = co.country_id
LEFT JOIN characteristics ch
ON r.character_id = ch.character_id;


-- DEMONSTRATION ON CREATING A FUNCTION --

-- The function below can be used for converting the grams in weight_in_grams column from the species table to kg.
-- Overall, converting the data in weight_in_grams can work better for the species table as there are more birds that are larger.

DELIMITER //

CREATE FUNCTION CalcWeightInKG (weight_in_grams INT)
RETURNS DECIMAL(5, 2)
DETERMINISTIC
BEGIN
    RETURN weight_in_grams / 1000;
END //

DELIMITER  ;

SELECT specie, CalcWeightInKg(weight_in_grams) AS weight_in_kg
FROM species;

-- DEMONSTRATION ON CREATING A STORED PROCEDURE
-- This stored procedure can be used when wanting to get individual information on each specie by their id with their characteristics.

DELIMITER //

CREATE PROCEDURE GetCharacteristicsBySpecieID(IN specie_id INT)
BEGIN
	SELECT * FROM characteristics WHERE character_id = specie_id;

END //

DELIMITER ;

CALL GetCharacteristicsBySpecieID(5);
