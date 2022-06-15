######################################
# Main function for project 
# Last Updated: 06/14/2022
#
#
#
######################################

from databaseEntry import databaseEntry
from dataHelperFunctions import databaseHelpers

#from flask import Flask

#app = Flask(__name__)

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
    zipCode = input("Enter a zip Code: ").strip()
    # TODO ask for time value 
    time = 0
    result = helper.getLatLongFromZip(zipCode)
    LongLat = list(result)
    results = helper.getEntryFromLonLat(LongLat, time)
    print(results.latitude_)

if __name__ == "__main__":
    main()