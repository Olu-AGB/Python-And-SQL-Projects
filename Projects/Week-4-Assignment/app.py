import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify, request
from config import db_config
from db_utils import insert_new_data



# Creating web application object

app = Flask(__name__)



############# CREATING HELPER FUNCTIONS #############

# The helper functions are created to aid the different endpoints I have created.

def get_connection():
    return mysql.connector.connect(**db_config)

def format_plane_arrivals(arrivals_row):
    if not arrivals_row:
        return None
    return {
        "plane_id": arrivals_row[0],
        "flight": arrivals_row[1],
        "coming_from": arrivals_row[2],
        "airport_code": arrivals_row[3],
        "airline": arrivals_row[4],
        "landed": arrivals_row[5],
        "on_time": arrivals_row[6],
    }

def format_plane_departures(departures_row):
    if not departures_row:
        return None
    return {
        "plane_id": departures_row[0],
        "flight": departures_row[1],
        "going_to": departures_row[2],
        "airport_code": departures_row[3],
        "airline": departures_row[4],
        "aircraft": departures_row[5],
        "departed": departures_row[6],
        "on_time": departures_row[7],
    }


############# CREATING API ENDPOINTS #################


# Creating API endpoint for homepage
@app.route("/")
def home():
    return {
        "message": "Welcome to the Plane Arrivals and Departures API!",
        "endpoints": {
            "GET /arrivals": "Gets all the plane arrivals data",
            "GET /departures": "Gets all the plane departures data",
            "GET /arrivals?limit=(a number)": "Gets a set amount of plane arrivals data",
            "GET /departures?limit=(a number)": "Gets a set amount of plane departures data",
            "POST /arrivals": "Adds new arrival data",
            "POST /departures": "Adds new departure data",
        }
    }




# Created an endpoint for viewing all the data from the table plane arrivals in the database airport_db, while also giving
# an option of using limit. The function get_plane_arrivals_records() connects to the database airport_db, uses SQL
# queries to retrieve data from the table, adds the limit if a limit is used, and returns the data in json format, with
# the status code 200 if no errors occur, otherwise it returns a message in json format including details about the error.
# Finally, since I am retrieving data, this would be a get request to the API, hence methods=["GET"].

@app.route("/arrivals", methods=["GET"])
def get_plane_arrivals_records(limit=None):
    print("Retrieving plane arrivals records...")

    try:
        limit = request.args.get("limit", default=None, type=int)

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""USE airport_db""")

            query_arrival = "SELECT * FROM plane_arrivals"
            if limit:
                query_arrival += f" LIMIT %s"
                cursor.execute(query_arrival, (limit,))
            else:
                cursor.execute(query_arrival)

            results_arrivals = cursor.fetchall()

            arrivals = []
            for row in results_arrivals:
                arrival = format_plane_arrivals(row)
                if arrival:
                    arrivals.append(arrival)

            return jsonify({
                "status": "success",
                "message": "Retrieved plane arrivals records.",
                "data": arrivals,
                "count": len(arrivals),
            }), 200
    except Error as e:
        print("Unexpected error:", e)
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve plane arrivals records",
            "error": e,
        }), 500


# Created an endpoint for viewing all the data from the table plane departures in the database airport_db. The function
# get_plane_departures_records() does everything like the function get_plane_arrivals_records but for the plane departures
# table instead.

@app.route("/departures", methods=["GET"])
def get_plane_departures_records(limit=None):
    print("Retrieving plane departures records...")

    try:
        limit = request.args.get("limit", default=None, type=int)

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""USE airport_db""")

            query_depart = "SELECT * FROM plane_departures"
            if limit:
                query_depart += f" LIMIT %s"
                cursor.execute(query_depart, (limit,))
            else:
                cursor.execute(query_depart)

            results_departures = cursor.fetchall()

            departures = []
            for row in results_departures:
                depart_rows = format_plane_departures(row)
                if depart_rows:
                    departures.append(depart_rows)

            return jsonify({
                "status": "success",
                "message": "Retrieved plane departures records.",
                "data": departures,
                "count": len(departures),
            }), 200
    except Error as e:
        print("Unexpected error:", e)
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve plane departures records",
            "error": e,
        }), 500


# Created an endpoint for inserting data into the plane arrivals table. The function insert_new_arrivals() validates the
# data, creates the fields to match with the columns in the plane arrivals table, returns the data with the new record
# when called from main.py if successful, hence also returning status code 200. If an error occurs, this will also be
# returned in json format with the satus code. Using methods=["POST"] allows data to be posted to the API.

@app.route("/arrivals", methods=["POST"])
def insert_new_arrivals():

    data = request.get_json()

    fields_arrivals = ["flight", "coming_from", "airport_code", "airline", "aircraft", "landed", "on_time"]
    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON body"
        }), 400

    for field in fields_arrivals:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"Field {field} is required."
            }), 400

    try:
        insert_data_arrivals = (
            data["flight"],
            data["coming_from"],
            data["airport_code"],
            data["airline"],
            data["aircraft"],
            data["landed"],
            data["on_time"]
        )

        insert_new_data("plane_arrivals", insert_data_arrivals)

        return jsonify({
            "status": "success",
            "message": "Successfully inserted new data into plane arrivals table",
            "data": insert_data_arrivals,
        }), 201


    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to insert new data into plane arrivals table",
            "error": str(e)
        }), 500


# Created an endpoint for inserting data into the plane departures table. The function insert_new_departures() does exactly
# the same things as the function insert_new_arrivals() does above, but for the columns in the plane departures table instead.

@app.route("/departures", methods=["POST"])
def insert_new_departures():

    data = request.get_json()

    fields_departures = ["flight", "going_to", "airport_code", "airline", "aircraft", "departed", "on_time"]
    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON body"
        }), 400

    for field in fields_departures:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"Field {field} is required."
            }), 400
    try:

        insert_data_departures = (
            data["flight"],
            data["going_to"],
            data["airport_code"],
            data["airline"],
            data["aircraft"],
            data["departed"],
            data["on_time"]
        )

        insert_new_data("plane_departures", insert_data_departures)

        return jsonify({
            "status": "success",
            "message": "Successfully inserted new data into plane departures table",
            "data": insert_data_departures,
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to insert new data into plane departures table",
            "error": str(e)
        }), 500


# For starting the server.

if __name__ == "__main__":
    app.run(debug=True)

