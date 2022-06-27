######################################
# Helper methods for the data-base 
# used for the project 
# Last Updated: 06/27/2022
#
#
#
######################################


from databaseEntry import databaseEntry
import sqlite3
import requests
import datetime

con = sqlite3.connect('SolarDatabase.db', check_same_thread=False)
cur = con.cursor()

class databaseHelpers:

    def convertDateToTime(self, date):
        # MM/DD/YYYY
        month = int(date[0] + date[1]) 
        day = int(date[3] + date[4])
        year = int(date[6] + date[7] + date[8] + date[9])
        dt = datetime.datetime(year, month, day)
        
        # need to be an int to cut off any decimal places 
        time = int(dt.timestamp())
        return time

    def convertTimeToDate(self, time):
        ts = int(time)
        date = datetime.datetime.fromtimestamp(ts)
        return date

    def callApi(self, Lat, Long, time):
        apiString = "http://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={long}&units={units}&dt={dt}&appid={API_key}".format(
                    lat = Lat, long = Long, units = "imperial", dt = time, API_key = "3c2a147d1d1f2209c45eb58546d9d49f")
        response = requests.get(apiString)
        if response.status_code == 200:
            # sucessfully fetched the data with parameters provided"
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
        ,?,?,?,?,?,?,?,?,?,?,?,?,?)", (round(entry.latitude_,4), round(entry.longitude_,4), entry.timeZone_, entry.timeZoneOffset_,
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
        cur.execute ("UPDATE raw_weather_json SET lat=?,lon=?,timezone=?,timezone_offset=?,dt=?,sunrise=?,\
            sunset=?,temp=?,feels_like=?,pressure=?,humidity=?,dew_point=?,uvi=?,clouds=?,visibility=?,wind_speed=?,\
            wind_deg=?,weather_id=?,weather_main=?,weather_description=?,weather_icon=? WHERE dt=?",
            (entry.latitude_, entry.longitude_, entry.timeZone_, entry.timeZoneOffset_,
            entry.data_.dateTime_, entry.data_.sunrise_, entry.data_.sunset_, entry.data_.temp_, entry.data_.feelsLike_,
            entry.data_.pressure_, entry.data_.humidity_, entry.data_.dewPoint_, entry.data_.uvi_, entry.data_.clouds_,
            entry.data_.visibility_, entry.data_.windSpeed_, entry.data_.windDeg_, entry.weather_.id_, entry.weather_.main_,
            entry.weather_.description_, entry.weather_.icon_, entry.data_.dateTime_))

         # Save (commit) the changes
        con.commit()

    # get a table from database to read
    def read(self):
        
        # get the table
        cur.execute("SELECT * FROM raw_weather_json")

        # turn into list of list
        values = []
        for row in cur:
            values = (list(row))

        return values 

    def getLatLongFromZip(self, zipcode):

        # Get long and lat from zip code table
        cur.execute("SELECT Lat,Lng FROM raw_us_zips WHERE zip=?", (zipcode,))

        # populate and return results
        longLat = []
        for row in cur:
            longLat = list(row)
        return longLat


    def getEntryFromLonLat(self, LatLong, time):
        
        # get entry for long and lat. Rounding to the 4th decimal place to match what was put in DataBase
        cur.execute("SELECT COUNT(*) FROM raw_weather_json WHERE lat=? and lon=? and dt=?", (round(LatLong[0],4), 
        round(LatLong[1],4), time))
        (number_of_rows,)=cur.fetchone()

        entry = databaseEntry()

        # not already in DB
        if (number_of_rows == 0):

            # Make Api Call
            apiResutls = self.callApi(LatLong[0], LatLong[1], time)

            data = apiResutls["data"]
            weather = (data[0]["weather"])

            # Fill out Databse Entry
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
            
            # add entry to the data base
            self.add(entry)

        else:
            # pull out DB entry
            cur.execute("SELECT * FROM raw_weather_json WHERE lat=? and lon=? and dt=?", (round(LatLong[0],4), 
            round(LatLong[1],4), time))

            values = []
            for row in cur:
                values = list(row)

            # Fill out Databse Entry
            entry.latitude_ = values[0]
            entry.longitude_ = values[1]
            entry.timeZone_ = values[2]
            entry.timeZoneOffset_ = values[3]
            entry.data_.dateTime_ = values[4]
            entry.data_.sunrise_ = values[5]
            entry.data_.sunset_ = values[6]
            entry.data_.temp_ = values[7]
            entry.data_.feelsLike_ = values[8]
            entry.data_.pressure_ = values[9]
            entry.data_.humidity_ = values[10]
            entry.data_.dewPoint_ = values[11]
            entry.data_.uvi_ = values[12]
            entry.data_.clouds_ = values[13]
            entry.data_.visibility_ = values[14]
            entry.data_.windSpeed_ = values[15]
            entry.data_.windDeg_ = values[16]
            entry.weather_.id_ = values[17]
            entry.weather_.main_ = values[18]
            entry.weather_.description_ = values[19]
            entry.weather_.icon_ = values[20]

        return entry