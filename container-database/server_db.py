# importing libraries
from sys import exec_prefix
from flask import Flask, request, jsonify
import sqlite3
import json


# creating constants
DB_NAME = "db/contacts.db"
COLUMNS = ["contact_id", "first_name", "last_name", "email", "phone"]

# creating the main application
app = Flask(__name__)

# create a connection to database
DB = sqlite3.connect(DB_NAME, check_same_thread=False)


# API call function to send all entries in DB
@app.route('/contacts_db', methods=["GET"])
def fill_table_db():
    global DB

    # Creating a query and execute it
    cursor = DB.cursor()
    query = "SELECT * FROM contacts;"
    cursor.execute(query)

    # convert the data into json format
    fetch_response = []
    i = 1
    for item in list(cursor.fetchall()):
        person = {"id": i, "first_name": item[0],
                  "last_name": item[1], "email": item[2], "phone": item[3]}
        fetch_response.append(person)
        i += 1

    cursor.close()
    return json.dumps(fetch_response)


# adding a new entry into database
@app.route('/add_entry_db', methods=["POST"])
def add_entry_db():
    global DB
    data = json.loads(request.data)

    data = (data['fname'], data['lname'], data['email'], data['phone'])
    attempt = True

    try:
        cursor_new_entry = DB.cursor()
        query_new_entry = "INSERT INTO contacts(first_name, last_name, email, phone) VALUES(?,?,?,?)"
        cursor_new_entry.execute(query_new_entry, data)
        DB.commit()
    except:
        DB.rollback()
        attempt = False
        pass

    resp = jsonify(success=attempt)
    return resp


# function to delete an entry
@app.route('/delete_db', methods=["POST"])
def delete_entry_db():
    global DB
    data = json.loads(request.data)
    data = (data['email'],)
    attempt = True

    try:
        cursor = DB.cursor()
        query = "DELETE FROM contacts WHERE email = ?"
        cursor.execute(query, data)
        DB.commit()
    except:
        DB.rollback()
        attempt = False
        pass

    resp = jsonify(success=attempt)
    return resp


if __name__ == "__main__":
    app.run(debug=True)
    # Stopping the cursor and closing the db
    DB.close()
