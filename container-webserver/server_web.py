# importing libraries
from sys import exec_prefix
from flask import Flask, request, render_template, jsonify
import requests
import json


# creating the main application
app = Flask(__name__)

# creating URL constants
MAIN_URL = "http://localhost:5000/"
URL_fill_table = MAIN_URL + "contacts_db"
URL_add_entry = MAIN_URL + "add_entry_db"
URL_delete_entry = MAIN_URL + "delete_db"


# Index function to retrieve the first web pag
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


# API call function to send all entries in DB
@app.route('/contacts', methods=["GET"])
def fill_table():
    global URL_fill_table
    # sending get request and saving the response as response object
    res = requests.get(url = URL_fill_table)
    # extracting data in json format
    data = res.json()
    
    #=================================
            #do some stuff here
    #=================================

    return json.dumps(data)


# adding a new entry into database
@app.route('/add_entry', methods=["POST"])
def add_entry():
    global URL_add_entry
    data = request.data
    # data = json.loads(request.data)
    
    #=================================
            #do some stuff here
    #=================================

    # making a post request to delete an entry
    r = requests.post(url = URL_add_entry, data = data)

    resp = jsonify(success = r.text)
    return resp


# function to delete an entry
@app.route('/delete', methods=["POST"])
def delete_entry():
    global URL_delete_entry
    data = request.data
    # data = json.loads(request.data)

    #=================================
            #do some stuff here
    #=================================

    # making a post request to delete an entry
    r = requests.post(url = URL_delete_entry, data = data)

    resp = jsonify(success=r.text)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
