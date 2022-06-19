######################################
# Main function for project 
# Last Updated: 06/18/2022
#
#
#
######################################

from databaseEntry import databaseEntry
from dataHelperFunctions import databaseHelpers


import sqlite3
from flask import Flask, render_template      

app = Flask(__name__)


con = sqlite3.connect('SolarDatbase.db')
cur = con.cursor()

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

#def addUser(email, username):

    # Insert a row of data
#    cur.execute("INSERT INTO testTable VALUES (?, ?)", (email, username))

    # Save (commit) the changes
#    con.commit()

def main():
    helper = databaseHelpers()
    zipCode = input("Enter a zip Code: ").strip()
    time = input("Enter a date (MM/DD/YYYY): ").strip()
    helper.convertDateToTime(time)
    result = helper.getLatLongFromZip(zipCode)
    LongLat = list(result)
    results = helper.getEntryFromLonLat(LongLat, time)


if __name__ == "__main__":
    app.run(debug=True)