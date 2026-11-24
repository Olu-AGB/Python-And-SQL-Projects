import requests
from pprint import pprint as pp

############## CLIENT SIDE INTERACTIONS ################


# Setting up Base URL
base_url = "http://127.0.0.1:5000"



# Function to view the data in plane arrivals from the API
def get_arrivals():
    response = requests.get(f"{base_url}/arrivals")
    print("Viewing arrivals data...")
    pp(response.json())

# Function to view the data in plane departures from the API
def get_departures():
    response = requests.get(f"{base_url}/departures")
    print("\n")
    print("Viewing departures data...")
    pp(response.json())



# Function for inserting data into the API endpoint in app.py by posting the user defined data from new_arrival to the
# endpoint. Try and except blocks are used for handling errors that may happen.
def insert_arrival():

    # ENTER NEW DATA HERE:
    new_arrival = {
        "flight": "MS783",
        "coming_from": "Cairo",
        "airport_code": "CAI",
        "airline": "Egyptair",
        "aircraft": "A20N",
        "landed": "2026-03-28 09:07:00",
        "on_time": True
    }

    try:
        response = requests.post(f"{base_url}/arrivals", json=new_arrival)

        response.raise_for_status()
        data = response.json()

        print("Inserting data into arrivals...")
        print("\n")
        pp(data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Function insert_departure() does exactly the same thing as the function above, insert_arrival(), but for the plane
# departures data instead.
def insert_departure():

    # ENTER NEW DATA HERE:
    new_departure = {
        "flight": "CX252",
        "going_to": "Hong Kong",
        "airport_code": "HKG",
        "airline": "Cathay Pacific",
        "aircraft": "B77W",
        "departed": "2026-03-28 12:35:00",
        "on_time": False
    }

    try:
        response = requests.post(f"{base_url}/departures", json=new_departure)

        response.raise_for_status()
        data = response.json()

        print("Inserting data into departures...")
        print("\n")
        pp(data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")




# Calling the functions

if __name__ == "__main__":
    get_arrivals()
    #get_departures()
    #insert_arrival()
    #insert_departure()
