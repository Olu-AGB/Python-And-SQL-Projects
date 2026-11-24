import mysql.connector
from config import db_config
from pprint import pprint as pp


############# CREATING airport_db DATABASE ################

def create_airport_db():
    try:
        db = mysql.connector.connect(**db_config) # Setting up connection
        cursor = db.cursor() # Using cursor as an object

        # Executing SQL queries for creating the database and tables
        cursor.execute("CREATE DATABASE IF NOT EXISTS airport_db")
        cursor.execute("USE airport_db")

        print("Database created successfully")

        tables = {
            "plane_arrivals": """ CREATE TABLE IF NOT EXISTS plane_arrivals (
                                     plane_id INT PRIMARY KEY AUTO_INCREMENT,
                                     flight VARCHAR(255) NOT NULL,
                                     coming_from VARCHAR(255),
                                     airport_code VARCHAR(255),
                                     airline VARCHAR(255),
                                     aircraft VARCHAR(255),
                                     landed DATETIME UNIQUE,
                                     on_time BOOLEAN
                              )""",

            "plane_departures": """ CREATE TABLE IF NOT EXISTS plane_departures (
                                       plane_id INT PRIMARY KEY AUTO_INCREMENT,
                                       flight VARCHAR(255) NOT NULL,
                                       going_to VARCHAR(255),
                                       airport_code VARCHAR(255),
                                       airline VARCHAR(255),
                                       aircraft VARCHAR(255),
                                       departed DATETIME UNIQUE,
                                       on_time BOOLEAN
                                )"""
        }

        # Creates the tables using the key:value pairs from the "table" dictionary above and executes the SQL queries
        # that are stored as values found in each key (plane_arrivals, plane_departures) that will define the columns of
        # both tables in the database.

        for name, query in tables.items():
            cursor.execute(query)
            print(f"Table {name} created successfully")

        # Inserting data into the newly created tables

        data_plane_arrivals = [
            ("LH2472", "Munich", "MUC", "Lufthansa", "A20N", "2026-03-28 09:27:00", True),
            ("EI162", "Dublin", "DUB", "Aer Lingus", "A21N", "2026-03-28 11:56:00", False),
            ("UA923", "Los Angeles", "LAX", "United Airlines", "B78X", "2026-03-28 09:35:00", True),
            ("BA296", "Chicago", "ORD", "British Airways", "B772", "2026-03-28 12:26:00", False),
            ("VS118", "Miami", "MIA", "Virgin Atlantic", "B789", "2026-03-28 12:06", True),
            ("FI450", "Reykjavik", "KEF", "Icelandair", "A21N", "2026-03-28 12:02:00", True),
            ("WS2", "Calgary", "YYC", "WestJet", "B789", "2026-03-28 11:40:00", True),
            ("SK531", "Stockholm", "ARN", "SAS", "A20N", "2026-03-28 14:56:00", False)
        ]

        data_plane_departures = [
            ("UA879", "Houston", "IAH", "United Airlines", "B772", "2026-03-28 10:17:00", True),
            ("BA396", "Cairo", "CAI", "British Airways", "A20N", "2026-03-28 10:37:00", True),
            ("AY1332", "Helsinki", "HEL", "Finnair", "A359", "2026-03-28 10:40:00", False),
            ("AA101", "New York", "JFK", "American Airlines", "B77W", "2026-03-28 10:41:00", False),
            ("AZ203", "Rome", "FCO", "ITA Airways", "A20N", "2026-03-28 10:47:00", False),
            ("VS302", "Delhi", "DEL", "Virgin Atlantic", "A35K", "2026-03-28 10:51:00", False),
            ("KM101", "Malta", "MLA", "KM Malta Airlines", "A20N", "2026-03-28 11:05:00", True),
            ("DL51", "Salt Lake City", "SLC", "Delta Air Lines", "A332", "2026-03-28 11:16:00", False)
        ]
        inserting_data_plane_arrivals = ("""INSERT INTO plane_arrivals (flight, coming_from, airport_code, airline, aircraft, landed, on_time)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s)""")
        inserting_data_plane_departures = ("""INSERT INTO plane_departures (flight, going_to, airport_code, airline, aircraft, departed, on_time)
                                              VALUES (%s, %s, %s, %s, %s, %s, %s)""")


        # Using cursor.executemany() to insert multiple rows at once into the table "plane_arrivals"

        plane_arrivals_rows = cursor.executemany(inserting_data_plane_arrivals, data_plane_arrivals)
        print("\n")
        print("Inserted data into table plane_arrivals successfully")
        print("\n")

        # Displaying the data stored in the "plane_arrivals" table

        cursor.execute("SELECT * FROM plane_arrivals")
        plane_arrivals_data = cursor.fetchall()
        print("Displaying plane_arrivals...")
        print("\n")
        pp(plane_arrivals_data)
        print("\n")


        # Using cursor.executemany() to insert multiple rows at once into the table "plane_departures"

        plane_departure_rows = cursor.executemany(inserting_data_plane_departures, data_plane_departures)
        print("Inserted data into table plane_departures successfully")
        print("\n")

        # Displaying the data stored in the "plane_departures" table

        cursor.execute("SELECT * FROM plane_arrivals")
        plane_arrivals_data = cursor.fetchall()
        print("Displaying plane_arrivals...")
        print("\n")
        pp(plane_arrivals_data)
        print("\n")



        db.commit()
        cursor.close()
        db.close()

    # Exception block used for if something goes wrong during the database creation

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")




def insert_new_data(table, data):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        cursor.execute("USE airport_db")

        if table == "plane_arrivals":
            query = f"""INSERT INTO plane_arrivals (flight, coming_from, airport_code, airline, aircraft, landed, on_time)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, data)

        elif table == "plane_departures":
            query = f"""INSERT INTO plane_departures (flight, going_to, airport_code, airline, aircraft, departed, on_time)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, data)

        print("Successfully inserted new data")

        db.commit()
        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        print(f"Failed to insert new data: {err}")




if __name__ == "__main__":
    create_airport_db()