######################################
# Helper methods for the data-base 
# used for the project 
# Last Updated: 06/14/2022
#
#
#
######################################


from ast import Delete
from re import A
from databaseEntry import databaseEntry, weather
import sqlite3
import requests

con = sqlite3.connect('SolarDatabase.db')
cur = con.cursor()

class databaseHelpers:

    def convertDateToTime(self, date):
        pass

    def callApi(self, Long, Lat, time):
        apiString = "http://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={long}&dt={dt}&appid={API_key}".format(
                    lat = Lat, long = Long, dt = time, API_key = "3c2a147d1d1f2209c45eb58546d9d49f")
        response = requests.get(apiString)
        if response.status_code == 200:
            #print("sucessfully fetched the data with parameters provided")
            return(response.json())
        else:
            print(f"There was a {response.status_code} error with the request")

    # Kill connection to dataBase
    def closeDataBase(self):
        cur.close()
        con.close()

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

        # turn into list of list
        values = []
        for row in cur:
            values.append(list(row))

        return values 

    def getLatLongFromZip(self, zipcode):

        # Get long and lat from zip code table
        cur.execute("SELECT Lat,Lng FROM raw_us_zips WHERE zip=?", (zipcode,))

        # populate and return results
        longLat = []
        for row in cur:
            longLat = list(row)
        return longLat


    def getEntryFromLonLat(self, LongLat, time):
        
        # get entry for long and lat
        cur.execute("SELECT * FROM raw_weather_json WHERE lat=? and lon=?", (LongLat[0],LongLat[1]))
        
        # Default to June 13, 12PM for now #TODO make time converter
        time = 1655136000

        # Make Api Call
        apiResutls = self.callApi(LongLat[0], LongLat[1], time)
        data = apiResutls["data"]
        weather = (data[0]["weather"])

        # Fill out Databse Entry
        entry = databaseEntry()
        entry.latitude_ = apiResutls["lat"]
        entry.longitude_ = apiResutls["lon"]
        entry.timeZone_ = apiResutls["timezone"]
        entry.timeZoneOffset_ = apiResutls["timezone_offset"]
        entry.data_.dateTime_ = data[0]["dt"]
        # TODO figure out why sunrise and sunset werent in call
        #entry.data_.sunrise_ = data[0]["sunrise"]
        #entry.data_.sunset_ = data[0]["sunset"]
        entry.data_.temp_ = data[0]["temp"]
        entry.data_.feelsLike_ = data[0]["feels_like"]
        entry.data_.pressure_ = data[0]["pressure"]
        entry.data_.humidity_ = data[0]["humidity"]
        entry.data_.dewPoint_ = data[0]["dew_point"]
        entry.data_.uvi_ = data[0]["uvi"]
        entry.data_.clouds_ = data[0]["clouds"]
        entry.data_.visibility_ = data[0]["visibility"]
        entry.data_.windSpeed_ = data[0]["wind_speed"]
        entry.data_.windDeg_ = data[0]["wind_deg"]
        entry.weather_.id_ = weather[0]["id"]
        entry.weather_.main_ = weather[0]["main"]
        entry.weather_.description_ = weather[0]["description"]
        entry.weather_.icon_ = weather[0]["icon"]

        return entry