import requests
import sys  # Newly added module. Allows you to interact with Python runtime environment.
import json
from pprint import pprint as pp

#############################
## Setting up the Base URL ##
#############################

base_url = "https://swapi.dev/api/"

response = requests.get(base_url)  # setting the response variable to request the url in the base_url variable
status_code = response.status_code  # creating the status_code variable to check status_code


# print(response.status_code) # status code 200 OK

# pp(response.json()) # prints root resource key-value pairs in json format


############################################################################
## Creating the functions for retrieving the data from the six attributes ##
############################################################################

# The functions get information for any given value on any of the six attributes from the base_url api,
# as long as the status code is 200
# e.g. film_id = 1 gives the url https://swapi.dev/api/films/1/
# To list everything, type in "/" as the argument when calling the functions e.g. pp(get_films_info("/")).


def get_films_info(film_id):
    films_url = f"{base_url}films/{film_id}/"
    films_response = requests.get(films_url)

    if films_response.status_code == 200:
        films_df = films_response.json()
        return films_df
    else:
        return f"Error in getting film info: {films_response.status_code}"


def get_people_info(people_id):
    people_url = f"{base_url}people/{people_id}/"
    people_response = requests.get(people_url)

    if people_response.status_code == 200:
        people_df = people_response.json()
        return people_df
    else:
        return f"Error in getting film info: {people_response.status_code}"


def get_planets_info(planets_id):
    planets_url = f"{base_url}planets/{planets_id}/"
    planets_response = requests.get(planets_url)

    if planets_response.status_code == 200:
        planets_df = planets_response.json()
        return planets_df
    else:
        return f"Error in getting film info: {planets_response.status_code}"


def get_species_info(species_id):
    species_url = f"{base_url}species/{species_id}/"
    species_response = requests.get(species_url)

    if species_response.status_code == 200:
        species_df = species_response.json()
        return species_df
    else:
        return f"Error in getting film info: {species_response.status_code}"


def get_starships_info(starships_id):
    starships_url = f"{base_url}starships/{starships_id}/"
    starships_response = requests.get(starships_url)

    if starships_response.status_code == 200:
        starships_df = starships_response.json()
        return starships_df
    else:
        return f"Error in getting film info: {starships_response.status_code}"


def get_vehicles_info(vehicles_id):
    vehicles_url = f"{base_url}vehicles/{vehicles_id}/"
    vehicles_response = requests.get(vehicles_url)

    if vehicles_response.status_code == 200:
        vehicles_df = vehicles_response.json()
        return vehicles_df
    else:
        return f"Error in getting film info: {vehicles_response.status_code}"


#################################################################
## Creating the variables to store the data from the functions ##
#################################################################

# xxx_info = dataframe e.g. vehicles_info = vehicles_df from get_vehicle_info("/")

films_info = get_films_info("/")  # people_id is "/"
people_info = get_people_info("/")
planets_info = get_planets_info("/")
species_info = get_species_info("/")
starships_info = get_starships_info("/")
vehicles_info = get_vehicles_info("/")

# pp(films_info)

#################################################
## Tidying the Dictionaries and Creating Lists ##
#################################################
#
# The code below gets the key "results" from the films_info dictionary to gain access tho the values that are
# dictionaries within themselves.
# Once these are stored in variables, create an empty list to append the fields_list which are field names in the
# data but narrowed down to keep the data consistent, then iterate through results_flims so that every [i] index in
# this data corresponds to the elements in fields_list and append these new values to the empty list films_list to store
# the different dictionaries as elements in the list.
# Process is repeated for the other 5 categories.

# Films List
results_films = films_info.get("results", [])
fields_list = ["episode_id", "title", "release_date", "director", "producer", "opening_crawl"]
films_list = []

for i in range(len(results_films)):
    film = results_films[i]
    films_dict = {field: film.get(field) for field in fields_list}
    films_list.append(films_dict)
    # pp(films_dict)
# pp(films_list)
# Writing to JSON File
with open("films.json", "w") as file:
    json.dump(films_list, file, indent=4)


# People List
results_people = people_info.get("results", [])
fields_people = ["name", "gender", "birth_year", "height", "mass", "skin_color", "eye_color"]
people_list = []

for i in range(len(results_people)):
    person = results_people[i]
    people_dict = {field: person.get(field) for field in fields_people}
    people_list.append(people_dict)
    # pp(people_dict)
# pp(people_list)
# Writing to JSON File
with open("people.json", "w") as file:
    json.dump(people_list, file, indent=4)


# Planets List
results_planets = planets_info.get("results", [])
fields_planets = ["name", "population", "terrain", "climate", "orbital_period", "rotation_period", "diameter",
                  "gravity", "surface_water"]
planets_list = []

for i in range(len(results_planets)):
    planet = results_planets[i]
    planets_dict = {field: planet.get(field) for field in fields_planets}
    planets_list.append(planets_dict)
    # pp(planets_dict)
# pp(planets_list)
# Writing to JSON File
with open("planets.json", "w") as file:
    json.dump(planets_list, file, indent=4)


# Species List
results_species = species_info.get("results", [])
fields_species = ["name", "classification", "designation", "average_lifespan", "average_height", "eye_colors",
                  "hair_colors", "language", "skin_colors"]
species_list = []

for i in range(len(results_species)):
    specie = results_species[i]
    species_dict = {field: specie.get(field) for field in fields_species}
    species_list.append(species_dict)
    # pp(species_dict)
# pp(species_list)
# Writing to JSON File
with open("species.json", "w") as file:
    json.dump(films_list, file, indent=4)


# Starships List
results_starships = starships_info.get("results", [])
fields_starships = ["name", "model", "starship_class", "manufacturer", "hyperdrive_rating", "MGLT", "cost_in_credits",
                    "cargo_capacity", "passengers", "consumables", "crew", "length", "max_atmosphering_speed"]
starships_list = []

for i in range(len(results_starships)):
    starship = results_starships[i]
    starships_dict = {field: starship.get(field) for field in fields_starships}
    starships_list.append(starships_dict)
    # pp(starships_dict)
# pp(starships_list)
# Writing to JSON File
with open("starships.json", "w") as file:
    json.dump(starships_list, file, indent=4)


# Vehicles List
results_vehicles = vehicles_info.get("results", [])
fields_vehicles = ["name", "model", "vehicle_class", "manufacturer", "length", "cargo_capacity", "cost_in_credits",
                   "crew", "passengers", "max_atmosphering_speed", "consumables"]
vehicles_list = []

for i in range(len(results_vehicles)):
    vehicle = results_vehicles[i]
    vehicles_dict = {field: vehicle.get(field) for field in fields_vehicles}
    vehicles_list.append(vehicles_dict)
    # pp(vehicles_dict)
# pp(vehicles_list)
# Writing to JSON File
with open("vehicles.json", "w") as file:
    json.dump(vehicles_list, file, indent=4)



###########################################
## Creating the function user_input_flag ##
###########################################

# Creating the function user_input_flag to redirect the code to the functions that correspond to the different
# categories but only if the user_input meets the conditions.

def user_input_flag(user_input):
    if user_input == "films":
        # pp(films_list)
        user_input_films_transition(films_list)

    if user_input == "people":
        # pp(people_list)
        user_input_people_transition(people_list)

    if user_input == "planets":
        # pp(planets_list)
        user_input_planets_transition(planets_list)

    if user_input == "species":
        # pp(species_list)
        user_input_species_transition(species_list)

    if user_input == "starships":
        # pp(starships_list)
        user_input_starships_transition(starships_list)

    if user_input == "vehicles":
        # pp(vehicles_list)
        user_input_vehicles_transition(vehicles_list)


##############################################################
## Creating the functions that correspond to the categories ##
##############################################################

# The next 6 functions represent the 6 categories.
# In each of these functions, this is where the user can decide what films, for example, they want to know more details
# of and whether they want to know about more than one film or go back to the main menu.
# The use of the while loop and if statements allow for this to happen, where if the conditions of the if statement in
# the while loop are met, the function will start again, and if not, the second question, 'user_options' will be
# displayed and depending on whether the conditions are met, it will either call the function 'user_input' to
# bring back the main menu or the program will end because of sys.exit().

def user_input_films_transition(films_data=films_list):
    print("\n")
    user_input_films = str(input("""
Choose what film you would like to know the details about by entering the number of the film:

1) 1
2) 2
3) 3
4) 4
5) 5
6) 6

Your choice: """))
    print("\n")

    if user_input_films == "1":
        pp(films_data[3])
    elif user_input_films == "2":
        pp(films_data[4])
    elif user_input_films == "3":
        pp(films_data[5])
    elif user_input_films == "4":
        pp(films_data[0])
    elif user_input_films == "5":
        pp(films_data[1])
    elif user_input_films == "6":
        pp(films_data[2])
    else:
        print("Please enter a valid choice.")

    print("\n")
    user_other_choices_films = str(input("""
Are there any other films you would like to know the details about?

1) yes
2) no

Your choice: """))
    print("\n")
    while True:
        if user_other_choices_films == "yes":
            user_input_films_transition(films_data=films_data)
            continue

        # print("\n")
        user_options = str(input("""
Are there any other categories you would like to know the details about?

1) yes
2) no

Your choice: """))
        print("\n")
        if user_options == "yes":
            user_input()
        else:
            sys.exit()


def user_input_people_transition(people_data=people_list):
    print("\n")
    user_input_people = str(input("""
What Star Wars character would you like to know the details about?

1) Luke Skywalker
2) C-3P0
3) R2-D2
4) Darth Vader
5) Leia Organa
6) Owen Lars
7) Beru Whitesun Lars
8) R5-D4
9) Biggs Darklighter
10) Obi-Wan Kenobi

Your choice: """))
    print("\n")

    if user_input_people == "Luke Skywalker":
        pp(people_data[0])
    elif user_input_people == "C-3P0":
        pp(people_data[1])
    elif user_input_people == "R2-D2":
        pp(people_data[2])
    elif user_input_people == "Darth Vader":
        pp(people_data[3])
    elif user_input_people == "Leia Organa":
        pp(people_data[4])
    elif user_input_people == "Owen Lars":
        pp(people_data[5])
    elif user_input_people == "Beru Whitesun Lars":
        pp(people_data[6])
    elif user_input_people == "R5-D4":
        pp(people_data[7])
    elif user_input_people == "Biggs Darklighter":
        pp(people_data[8])
    elif user_input_people == "Obi-Wan Kenobi":
        pp(people_data[9])
    else:
        print("Please enter a valid choice.")

    print("\n")
    user_other_choices_people = str(input("""
Are there any other characters you would like to know the details about?

1) yes
2) no

Your choice: """))
    print("\n")
    while True:
        if user_other_choices_people == "yes":
            user_input_people_transition(people_data=people_data)
            continue

        user_options = str(input("""
Are there any other categories you would like to know the details about?

1) yes
2) no

Your choice: """))
        print("\n")
        if user_options == "yes":
            user_input()
        else:
            sys.exit()


def user_input_planets_transition(planets_data=planets_list):
    print("\n")
    user_input_people = str(input("""
What Star Wars Planets would you like to know the details about?

1) Tatooine
2) Alderaan
3) Yavin IV
4) Hoth
5) Degobah
6) Bespin
7) Endor
8) Naboo
9) Coruscant
10) Kamino

Your choice: """))
    print("\n")

    if user_input_people == "Tatooine":
        pp(planets_data[0])
    elif user_input_people == "Alderaan":
        pp(planets_data[1])
    elif user_input_people == "Yavin IV":
        pp(planets_data[2])
    elif user_input_people == "Hoth":
        pp(planets_data[3])
    elif user_input_people == "Degobah":
        pp(planets_data[4])
    elif user_input_people == "Bespin":
        pp(planets_data[5])
    elif user_input_people == "Endor":
        pp(planets_data[6])
    elif user_input_people == "Naboo":
        pp(planets_data[7])
    elif user_input_people == "Coruscant":
        pp(planets_data[8])
    elif user_input_people == "Kamino":
        pp(planets_data[9])
    else:
        print("Please enter a valid choice.")

    print("\n")
    user_other_choices_planets = str(input("""
Are there any other planets you would like to know the details about?

1) yes
2) no

Your choice: """))
    print("\n")
    while True:
        if user_other_choices_planets == "yes":
            user_input_planets_transition(planets_data=planets_data)
            continue

        user_options = str(input("""
Are there any other categories you would like to know the details about?

1) yes
2) no

Your choice: """))
        print("\n")
        if user_options == "yes":
            user_input()
        else:
            sys.exit()


def user_input_species_transition(species_data=species_list):
    print("\n")
    user_input_species = str(input("""
What Star Wars Species characteristics would you like to know the details about?

1) Human
2) Droid
3) Wookie
4) Rodian
5) Hutt
6) Yoda's species
7) Trandoshan
8) Mon Calamari
9) Ewok
10) Sullustan

Your choice:  """))
    print("\n")

    if user_input_species == "Human":
        pp(species_data[0])
    elif user_input_species == "Droid":
        pp(species_data[1])
    elif user_input_species == "Wookie":
        pp(species_data[2])
    elif user_input_species == "Rodian":
        pp(species_data[3])
    elif user_input_species == "Hutt":
        pp(species_data[4])
    elif user_input_species == "Yoda's species":
        pp(species_data[5])
    elif user_input_species == "Trandoshan":
        pp(species_data[6])
    elif user_input_species == "Mon Calamari":
        pp(species_data[7])
    elif user_input_species == "Ewok":
        pp(species_data[8])
    elif user_input_species == "Sullustan":
        pp(species_data[9])
    else:
        print("Please enter a valid choice.")

    print("\n")
    user_other_choices_species = str(input("""
Are there any other species you would like to know the details about?

1) yes
2) no

Your choice: """))
    print("\n")
    while True:
        if user_other_choices_species == "yes":
            user_input_species_transition(species_data=species_data)
            continue

        user_options = str(input("""
Are there any other categories you would like to know the details about?

1) yes
2) no

Your choice: """))
        print("\n")
        if user_options == "yes":
            user_input()
        else:
            sys.exit()


def user_input_starships_transition(starships_data=starships_list):
    print("\n")
    user_input_starships = str(input("""
What Star Wars Starships would you like to know the details about?

1) CR90 corvette
2) Star Destroyer
3) Sentinel-class landing craft
4) Death Star
5) Millennium Falcon
6) Y-wing
7) X-wing
8) TIE Advanced x1
9) Executor
10) Rebel transport

Your choice: """))
    print("\n")

    if user_input_starships == "CR90 corvette":
        pp(starships_data[0])
    elif user_input_starships == "Star Destroyer":
        pp(starships_data[1])
    elif user_input_starships == "Sentinel-class landing craft":
        pp(starships_data[2])
    elif user_input_starships == "Death Star":
        pp(starships_data[3])
    elif user_input_starships == "Millennium Falcon":
        pp(starships_data[4])
    elif user_input_starships == "Y-wing":
        pp(starships_data[5])
    elif user_input_starships == "X-wing":
        pp(starships_data[6])
    elif user_input_starships == "TIE Advanced x1":
        pp(starships_data[7])
    elif user_input_starships == "Executor":
        pp(starships_data[8])
    elif user_input_starships == "Rebel transport":
        pp(starships_data[9])
    else:
        print("Please enter a valid choice.")

    print("\n")
    user_other_choices_starships = str(input("""
Are there any other starships you would like to know the details about?

1) yes
2) no

Your choice: """))
    print("\n")
    while True:
        if user_other_choices_starships == "yes":
            user_input_starships_transition(starships_data=starships_data)
            continue

        user_options = str(input("""
Are there any other categories you would like to know the details about?

1) yes
2) no

Your choice: """))
        print("\n")
        if user_options == "yes":
            user_input()
        else:
            sys.exit()


def user_input_vehicles_transition(vehicles_data=vehicles_list):
    print("\n")
    user_input_vehicles = str(input("""
What Star Wars Vehicles would you like to know the details about?

1) Sand Crawler
2) T-16 skyhopper
3) X-34 landspeeder
4) TIE/LN starfighter
5) Snowspeeder
6) TIE bomber
7) AT-AT
8) AT-ST
9) Storm IV Twin-Pod cloud car
10) Sail barge

Your choice: """))
    print("\n")

    if user_input_vehicles == "Sand Crawler":
        pp(vehicles_data[0])
    elif user_input_vehicles == "T-16 skyhopper":
        pp(vehicles_data[1])
    elif user_input_vehicles == "X-34 landspeeder":
        pp(vehicles_data[2])
    elif user_input_vehicles == "TIE/LN starfighter":
        pp(vehicles_data[3])
    elif user_input_vehicles == "Snowspeeder":
        pp(vehicles_data[4])
    elif user_input_vehicles == "TIE bomber":
        pp(vehicles_data[5])
    elif user_input_vehicles == "AT-AT":
        pp(vehicles_data[6])
    elif user_input_vehicles == "AT-ST":
        pp(vehicles_data[6])
    elif user_input_vehicles == "Storm IV Twin-Pod cloud car":
        pp(vehicles_data[8])
    elif user_input_vehicles == "Sail barge":
        pp(vehicles_data[9])
    else:
        print("Please enter a valid choice.")

    print("\n")
    user_other_choices_vehicles = str(input("""
Are there any other vehicles you would like to know the details about?

1) yes
2) no

Your choice: """))
    print("\n")
    while True:
        if user_other_choices_vehicles == "yes":
            user_input_vehicles_transition(vehicles_data=vehicles_data)
            continue

        user_options = str(input("""
Are there any other categories you would like to know the details about?

1) yes
2) no

Your choice: """))
        print("\n")
        if user_options == "yes":
            user_input()
        else:
            sys.exit()


############## STAR WARS API DATA RETRIEVER SYSTEM ##############

# The fundamental part of the code.
# This is where I initialise the first user input where it asks to choose from the categories.
# If the user chose 'none', the message will print and the program will end from sys.exit().
# The function returns 'user_input' so it can be used in the other functions.

def user_input():
    print("\n")
    user_input = str(input("""Welcome to Star Wars API Data Retriever!\n
Please choose from the following categories:\n
1) films\n
2) people\n
3) planets\n
4) species\n
5) starships\n
6) vehicles\n
7) none

Your choice: """))
    print("\n")
    if user_input == "none":
        print("See you later!")
        sys.exit()
    else:
        user_input_flag(user_input)

    return user_input


user_input()  # starts the script from line 193 onwards
