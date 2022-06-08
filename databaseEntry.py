######################################
# Structure for the database Entry
# Last Updated: 06/06/2022
#
#
#
######################################

class weather:
    def __init__(self):
        self.id_ = 0
        self.main_ = ""
        self.description_ = ""
        self.icon_ = ""

class weatherData:
    def __init__(self):
        self.dateTime_ = 0
        self.sunrise_ = 0
        self.sunset_ = 0
        self.temp_ = 0
        self.feelsLike_ = 0
        self.pressure_ = 0
        self.humidity_ = 0
        self.dewPoint_ = 0
        self.uvi_ = 0
        self.clouds_ = 0
        self.visibility_ = 0
        self.windSpeed_ = 0
        self.windDeg_ = 0 

class databaseEntry:

     # Default constructor
    def __init__(self):
        self.latatiude_ = 0
        self.longitude_ = 0
        self.timeZone_ = ""
        self.timeZoneOffset_ = 0
        self.data_ = weatherData()
        self.weather_ = weather()