######################################
# Calculations for if Solar panels are worth it
# Last Updated: 07/03/2022
#
#
#
######################################

from datetime import datetime

class SunLightAlgorithm:

    def getTotalSunlightForWeek(self, dates):
        totalSunLight = 0
        for day in dates:

            sunRise = day.data_.sunrise_.replace (':','')
            timeOfSunrise = 0
            if (sunRise[0] == "1"):
                hourRise = int(sunRise[0] + sunRise[1])
                if (hourRise == 12):
                    hourRise = 0 # for Midnight 
                minuteRise = int(sunRise[2] + sunRise[3])
                secondRise = int(sunRise[4] + sunRise[5])
            else:
                hourRise = int(sunRise[0])
                minuteRise = int(sunRise[1] + sunRise[2])
                secondRise = int(sunRise[3] + sunRise[4])
            if ((sunRise[-2] + sunRise[-1]) == "AM"):
                timeOfSunrise = (hourRise * 3600) + (minuteRise * 60) + secondRise
            else: #PM
                timeOfSunrise = (12 * 3600) + (hourRise * 3600) + (minuteRise * 60) + secondRise

            sunSet = day.data_.sunset_.replace (':','')
            timeOfSunset = 0

            if (sunSet[0] == "1"):
                hourSet = int(sunSet[0] + sunSet[1])
                if (hourSet == 12):
                    hourSet = 24 # for Midnight 
                minuteSet = int(sunSet[2] + sunSet[3])
                secondSet = int(sunSet[4] + sunSet[5])
            else:
                hourSet = int(sunSet[0])
                minuteSet = int(sunSet[1] + sunSet[2])
                secondSet = int(sunSet[3] + sunSet[4])
            if ((sunRise[-2] + sunRise[-1]) == "AM"):
                timeOfSunset = (hourSet * 3600) + (minuteSet * 60) + secondSet
            else: #PM
                timeOfSunset = (12 * 3600) + (hourSet * 3600) + (minuteSet * 60) + secondSet
            totalSunLight += (timeOfSunset - timeOfSunrise)

        hours = totalSunLight // 3600
        secondsLeft = totalSunLight % 3600
        minutes = secondsLeft // 60
        seconds = secondsLeft % 60 
        return [hours, minutes, seconds]

