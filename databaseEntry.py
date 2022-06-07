######################################
# Structure for the database Entry
# Last Updated: 06/06/2022
#
#
#
######################################


class weatherData:
    def __init__(self):
        self.dateTime_ = 0
        self.sunrise_ = 0

class databaseEntry:

     # Default constructor
    def __init__(self):
        self.latatiude_ = 0
        self.longitude_ = 0
        self.timeZone_ = ""
        self.timeZoneOffset_ = 0
        self.data_ = weatherData()