# Airport Database API Arrivals and Departures System

Welcome to Airport Arrivals and Departures API! This API system allows you to interact with the data. You can view the\
data in each table which you can choose to use a limit, or you can add new data to each table.

## How to Interact With the API

The API works with four files: **config.py**, **db_utils.py**, **app.py** and **main.py**.

- **config.py**: The file will show up as config_here_example.py. Here in this file, enter your SQL server connection details\
             and rename the file to config.py.
#
- **db_utils.py**: This file contains all the SQL queries that are used to interact with the database. This is where the database\
               gets created, as well as the tables. This file also contains the function for inserting data into the tables.
#
- **app.py**: This is where the application is run. This file contains the API Endpoints required for interactions. This is\
          also where the API Flask web framework gets created.
#
- **main.py**: This file contains the functions required for calling the API Endpoints and enables changes to be made to the data.
#

First, open the **config_here_example.py** file, enter your details, and rename the file to **config.py**. Next, you should\
open **db_utils.py** to establish a connection with SQL and run the file to create the database. Once this has been done,\
you should open the **app.py** file and run it to create the url. This is where you can enter the different pathways based\
on the endpoints I have created. Finally, open the **main.py** and start running some of the functions I have listed to\
start viewing the data or inserting data. In order to see the new changes from inserting data, first run **app.py**, click\
on the link, go back to **main.py** and run either insert_arrival() or insert_departure() and then type into the url to see\
the changes made.

Furthermore, I have created an **airport_db.sql** file as reference to the database I created in python, which can be run\
in MYSQL Workbench. I have also created a **requirements.txt** file while lists all the modules I used and their versions\
that I used in my code. The **.gitignore** file was also shared containing the file to ignore.
#




## Creative Scenario 
Airport arrivals and departures system. This API will allow users to view flight records on arrivals and departures\
from an airport and to add data to each of these tables. I will create a configuration file containing the details required\
for connecting to sql, and using the module mysql.connector, I will write SQL queries in Python in a file called db_utils.py\
to create the database airport_db and the two tables, plane arrivals and plane departures. This file will also include the\
queries for inserting data into each table so that this can be used with the API endpoints in app.py, which can then be called\
in the client-side file, main.py. This will also users to view the data in both tables and insert data.



