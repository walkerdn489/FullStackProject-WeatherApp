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

        self.assertEqual(values[0], 1, "longitude should be 1")
        self.assertEqual(values[1], 1, "latitude should be 1")
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
        listResults = list(result)
        print(listResults)

if __name__ == '__main__':
    unittest.main()