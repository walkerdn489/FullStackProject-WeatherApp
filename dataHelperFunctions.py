######################################
# Helper methods for the data-base 
# used for the project 
# Last Updated: 06/06/2022
#
#
#
######################################


from ast import Delete
from databaseEntry import databaseEntry
import sqlite3

con = sqlite3.connect('SolarDatabase.db')
cur = con.cursor()

class databaseHelpers:

    # add element to the database
    def add(self, entry):

         # Insert a row of data
        cur.execute("INSERT INTO raw_weather_json VALUES (?,?,?,?,?,?,?,? \
        ,?,?,?,?,?,?,?,?,?,?,?,?,?)", (entry.latitude_, entry.longitude_, entry.timeZone_, entry.timeZoneOffset_,
            entry.data_.dateTime_, entry.data_.sunrise_, entry.data_.sunset_, entry.data_.temp_, entry.data_.feelsLike_,
            entry.data_.pressure_, entry.data_.humidity_, entry.data_.dewPoint_, entry.data_.uvi_, entry.data_.clouds_,
            entry.data_.visibility_, entry.data_.windSpeed_, entry.data_.windDeg_, entry.weather_.id_, entry.weather_.main_,
            entry.weather_.description_, entry.weather_.icon_))

        # Save (commit) the changes
        con.commit()
    
    # remove element from the database
    def delete(self, entry):

        # delete a row of data
        cur.execute("DELETE FROM raw_weather_json WHERE lat=? and lon=? and dt=?", (entry.latitude_, entry.longitude_,
        entry.data_.dateTime_))

        # Save (commit) the changes
        con.commit()
    
    # update an emelent in the database
    def update(self, entry):
        pass

    # get a table from database to read
    def read(self):
        
        # get the table
        cur.execute("SELECT * FROM raw_weather_json")

        # Save (commit) the changes
        con.commit()

    def getLatLongFromZip(self, zipcode):
        cur.execute("SELECT Lat,Lng FROM raw_us_zips WHERE zip=?", (zipcode,))
        longLat = []
        for row in cur:
            longLat = list(row)
        return longLat