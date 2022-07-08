######################################
# Calculations for if Solar panels are worth it
# Last Updated: 07/03/2022
#
#
#
######################################

class SunLightAlgorithm:

    def getTotalSunlightForWeek(self, dates):
        totalSunLight = 0
        for day in dates:
            print(day.data_.sunset_,  day.data_.sunrise_)
            #totalSunLight += day.data_.sunset_ - day.data_.sunrise_
        print(totalSunLight)