######################################
# Unit test for dataHelperFunctions
# Last Updated: 06/27/2022
#
#
#
######################################i

import unittest
from databaseEntry import databaseEntry
from dataHelperFunctions import databaseHelpers

import sqlite3

con = sqlite3.connect('SolarDatabase.db')
cur = con.cursor()

class TestAddAndDeleteToDataBase(unittest.TestCase):
    helper = databaseHelpers()
    entry = databaseEntry()
    entry.longitude_ = 1
    entry.latitude_ = 1
    entry.timeZone_ = "EST"
    entry.data_.dateTime_ = 1
    entry.data_.temp_ = 290
    entry.weather_.description_ = "cloudy"
    entry.weather_.id_ = 1
    
    def test_addToDataBase(self):
        self.helper.add(self.entry)

        # get the element
        cur.execute("SELECT * FROM raw_weather_json WHERE dt=?", (self.entry.data_.dateTime_,))

        values = []
        for row in cur:
            values = list(row)

        self.assertEqual(values[0], 1, "latitude_ should be 1")
        self.assertEqual(values[1], 1, "longitude should be 1")
        self.assertEqual(values[2], "EST", "TimeZone should be EST")
        self.assertEqual(values[3], 0, "timeZoneOffset is empty")
        self.assertEqual(values[4], 1, "dataTime is 1")
        self.assertEqual(values[5], 0, "sunrise is empty")
        self.assertEqual(values[6], 0, "sunset is empty")
        self.assertEqual(values[7], 290, "temp is 290k")
        self.assertEqual(values[8], 0, "feeslike is empty")
        self.assertEqual(values[9], 0, "pressure is empty")
        self.assertEqual(values[10], 0, "humidity is empty")
        self.assertEqual(values[11], 0, "dewpoint is empty")
        self.assertEqual(values[12], 0, "uvi is empty")
        self.assertEqual(values[13], 0, "clouds is empty")
        self.assertEqual(values[14], 0, "visibility is empty")
        self.assertEqual(values[15], 0, "windspeed is empty")
        self.assertEqual(values[16], 0, "winddeg is empty")
        self.assertEqual(values[17], 1, "id is 1")
        self.assertEqual(values[18], "", "main is empty")
        self.assertEqual(values[19], "cloudy", "description is cloudy")
        self.assertEqual(values[20], "", "icon is empty")

    def test_deleteFromDataBase(self):
        self.helper.delete(self.entry)

        # get the element
        cur.execute("SELECT * FROM raw_weather_json WHERE dt=?", (self.entry.data_.dateTime_,))

        values = []
        for row in cur:
            values = list(row)
            
        self.assertEqual(len(values), 0, "should not find entry since it is deleted")
    
class TestGetLonLatFromZip(unittest.TestCase):
    helper = databaseHelpers()

    def test_getLonLat(self):
        zipCode = 29910
        result = self.helper.getLatLongFromZip(zipCode)
        self.assertEqual(result[0], 32.2204, "Latitude should be 32.2204")
        self.assertEqual(result[1], -80.88277, "Longitude should be -80.88277")

class TestDateTimeConversions(unittest.TestCase):
    helper = databaseHelpers()

    def test_TimeConversions(self):
        date = "05/18/1998"
        time = self.helper.convertDateToTime(date)

        #This is based on time zone when running
        offset = 0
        time = time - offset
        self.assertEqual(time, 895464000.0,"Time should be around 895464000.0 seconds")
        
        # May 18th 1998
        date = self.helper.convertTimeToDate(time)
        date = date.strftime('%m/%d/%Y')
        month = date[0] + date[1]
        day = date[3] + date[4]
        year = date[6] + date[7] + date[8] + date[9]
        self.assertEqual(month, "05", "Month should be May") 
        self.assertEqual(day, "18", "Day should be 18th")
        self.assertEqual(year, "1998", "Year should be 1998")


class TestUpdateToDataBase(unittest.TestCase):
    helper = databaseHelpers()
    entry = databaseEntry()
    entry.longitude_ = 1
    entry.latitude_ = 1
    entry.timeZone_ = "EST"
    entry.data_.dateTime_ = 1
    entry.data_.temp_ = 290
    entry.weather_.description_ = "cloudy"
    entry.weather_.id_ = 1

    def test_updateToDataBase(self):

        self.helper.add(self.entry)

        self.entry.longitude_ = 2
        self.helper.update(self.entry)

        # get the element
        cur.execute("SELECT * FROM raw_weather_json WHERE dt=?", (self.entry.data_.dateTime_,))

        values = []
        for row in cur:
            values = list(row)
        self.assertEqual(values[1], 2, "longitude should now be 2")

        self.helper.delete(self.entry)        

class TestGetDBEntryFromLatLong(unittest.TestCase):
    helper = databaseHelpers()
    entry = databaseEntry()

    def test_GetDBEntryFromLatLong(self):
        date = "06/26/2022"
        latLong = self.helper.getLatLongFromZip("01752")

        # First time should add it to DB 
        results = self.helper.getEntryFromLonLat(latLong, date)

        # Second time should pull it out of DB 
        secondResults = self.helper.getEntryFromLonLat(latLong, date)

        self.assertEqual(results.latitude_, secondResults.latitude_, 42.3494)
        self.assertEqual(results.longitude_, secondResults.longitude_, -71.5468)
        self.assertEqual(results.timeZone_,secondResults.timeZone_,"America/New_York")
        self.assertEqual(results.data_.dateTime_, secondResults.data_.dateTime_, 1656216000)
        self.assertEqual(results.data_.temp_, secondResults.data_.temp_,66.2)


if __name__ == '__main__':
    unittest.main()