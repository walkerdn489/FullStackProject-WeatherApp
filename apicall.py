import requests
import calendar 
import time

# lat long for zipcode 29302
lat = 34.89399
lng = -81.84151
api_key = "fee8e2aec4f405cbdfd44c35e8de2080"

# Convert from epoch to human-readable date
#import time; time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))

# Convert from human-readable date to epoch
# calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))

date_weather = input("Enter date you want the weather(i.e 2022-01-01 12:00:00): ")

epoch_datetime = calendar.timegm(time.strptime(date_weather, '%Y-%m-%d %H:%M:%S')) 


api_string = "http://api.openweathermap.org/data/3.0/onecall/timemachine?lat={}&lon={}&dt={}&appid={}".format(lat,lng,epoch_datetime,api_key)

response = requests.get(api_string)

with open('api_text.txt', 'w') as f:
    f.write(str(response.json()))