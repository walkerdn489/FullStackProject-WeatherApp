######################################
# Helper methods for the data-base 
# used for the project 
# Last Updated: 07/03/2022
#
#
#
######################################

from datetime import datetime, timezone
import DataBaseMethods
import requests

class databaseHelpers:

    ############################
    # Function: convertDateToTime
    #
    # Input: date - A given date to convert to unix time. MM/DD/YYYY
    #
    # Output: a unix time. 
    #
    # Notes:  
    ############################
    def convertDateToTime(self, date):
        # MM/DD/YYYY
        month = int(date[0] + date[1]) 
        day = int(date[3] + date[4])
        year = int(date[6] + date[7] + date[8] + date[9])
        dt = datetime(year, month, day)
        # Make sure time is in UTC
        dt = dt.replace(tzinfo=timezone.utc)
        
        # need to be an int to cut off any decimal places 
        time = int(dt.timestamp())
        return time

    ############################
    # Function: convertTimeToDate
    #
    # Input: a unix time 
    #
    # Output: the date MM/DD?YYY that represents the given Unix time
    #
    # Notes:  
    ############################
    def convertTimeToDate(self, time):
        ts = int(time)
        # make sure date is in utc
        date = datetime.fromtimestamp(ts, timezone.utc)
        return date

    ############################
    # Function: __callApi
    #
    # Input: lat: Latitude, long: Longitude, time: Unix time
    #
    # Output: response for the open weather map api
    #
    # Notes:  
    # This is a Private method (__FUNCTION_NAME)
    ############################
    def __callApi(self, lat, long, time):
        apiString = "http://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={long}&units={units}&dt={dt}&appid={API_key}".format(
                    lat = lat, long = long, units = "imperial", dt = time, API_key = "3c2a147d1d1f2209c45eb58546d9d49f")
        response = requests.get(apiString)
        if response.status_code == 200:
            # successfully fetched the data with parameters provided"
            return(response.json())
        else:
            print(f"There was a {response.status_code} error with the request")

    #############################
    # Function: __callSunRiseSetApi
    #
    # Input: lat: Latitude, long: Longitude, date: MM/DD/YYYY
    #
    # Output: Response from sunrise sunset api
    #
    # Notes:  
    # This is a Private method (__FUNCTION_NAME)
    # This comes out in UTC
    ############################
    def __callSunRiseSetApi(self, lat, long, date): 
        # Change Date to YYYY-MM-DD
        month = date[0] + date[1]
        day = date[3] + date[4]
        year = date[6] + date[7] + date[8] + date[9]
        date = year + "-" + month + "-" + day
        apiString = "https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&date={date}".format(
                    lat = lat, long = long, date = date)
        response = requests.get(apiString)
        if response.status_code == 200:
            # successfully fetched the data with parameters provided"
            return(response.json())
        else:
            print(f"There was a {response.status_code} error with the request")

    def getDaysOfCurrentWeek(self, date):
        dates = [date]
        time = self.convertDateToTime(date)
        i = 1
        while (i < 7):
            # 86,400 seconds in a day
            time = time - 86400
            day = self.convertTimeToDate(time)
            day = day.strftime('%m/%d/%Y')
            dates.append(day)
            i = i + 1
        return dates