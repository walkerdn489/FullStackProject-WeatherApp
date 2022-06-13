
import sqlite3
from databaseEntry import databaseEntry
from dataHelperFunctions import databaseHelpers

#from flask import Flask

#app = Flask(__name__)

con = sqlite3.connect('SolarDatabase.db')
cur = con.cursor()

#def addUser(email, username):

    # Insert a row of data
#    cur.execute("INSERT INTO testTable VALUES (?, ?)", (email, username))

    # Save (commit) the changes
#    con.commit()

#@app.route('/')
#def hello():
#    return '<h1>Hello, World!</h1>'

def main():
    helper = databaseHelpers()
    zipCode = input("Enter a zip Code")
    result = helper.getLatLongFromZip(zipCode)
    listResults = list(result)
    

if __name__ == "__main__":
    main()