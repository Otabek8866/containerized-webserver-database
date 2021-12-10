# importing libraries
from flask import Flask, request, render_template
import sqlite3
import json


# creating constants
DB_NAME = "db/contacts.db"
COLUMNS = ["contact_id", "first_name", "last_name", "email", "phone"]

# creating the main application
app = Flask(__name__)

# create a connection to database
DB = sqlite3.connect(DB_NAME, check_same_thread=False)


# Index function to retrieve the first web pag
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


# API call function to send all entries in DB
@app.route('/contacts', methods=["GET"])
def fill_table():
    global DB

    # Creating a query and execute it
    cursor = DB.cursor()
    query = "SELECT * FROM contacts;"
    cursor.execute(query)

    # convert the data into json format
    fetch_response = []
    for item in list(cursor.fetchall()):
        person = {"id": item[0], "first_name": item[1],
                  "last_name": item[2], "email": item[3], "phone": item[4], }
        fetch_response.append(person)

    cursor.close()
    return json.dumps(fetch_response)


@app.route('/add_entry', methods=["POST"])
def add_entry():
    print(request)
    print(request.args.get("fname"))
    return render_template("index.html")


@app.route('/<int:id>', methods=["POST"])
def second_page_sliding(id):
    # id = int(id)
    pass


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)

    # Stopping the cursor and closing the db
    DB.close()
