######################################
# Structure for the database Entry
# Last Updated: 06/13/2022
#
#
#
######################################

class weather:
    def __init__(self):
        # Weather condition code
        self.id_ = 0

        # Group of weather parameters (Rain, Snow, Extreme etc.)
        self.main_ = ""

        #  Weather condition within the group
        self.description_ = ""

        # Weather icon id
        self.icon_ = ""

class weatherData:
    def __init__(self):
        # date time, Unix, UTC
        self.dateTime_ = 0

        # Time of sunrise in UTC
        self.sunrise_ = 0

        # Time of sunset in UTC
        self.sunset_ = 0

        # Temperature. Units – measured in Fahrenheit
        self.temp_ = 0

        # Temperature. This accounts for the human perception, measured in Fahrenheit
        self.feelsLike_ = 0

        # Atmospheric pressure on the sea level, hPa
        self.pressure_ = 0

        # Humidity, %
        self.humidity_ = 0

        # Atmospheric temperature (varying according to pressure and humidity) 
        # below which water droplets begin to condense and dew can form. 
        # Units – measured in Fahrenheit.
        self.dewPoint_ = 0

        # UV index
        self.uvi_ = 0

        # Cloudiness, %
        self.clouds_ = 0

        # Average visibility, metres. The maximum value of the visibility is 10km
        self.visibility_ = 0
        
        # Wind speed. Units – miles/hour
        self.windSpeed_ = 0

        # Wind direction, degrees (meteorological)
        self.windDeg_ = 0 

class databaseEntry:

     # Default constructor
    def __init__(self):
        # Latitude of the Area 
        self.latitude_ = 0

        # Longitude of the Area
        self.longitude_ = 0

        # Timezone of area. "EST", "UTC", etc.
        self.timeZone_ = ""

        # the difference in hours and minutes between a particular time zone and UTC.
        self.timeZoneOffset_ = 0

        # Data on the weather
        self.data_ = weatherData()

        # Weather descriptions 
        self.weather_ = weather()