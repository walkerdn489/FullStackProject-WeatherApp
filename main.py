######################################
# Main function for project 
# Last Updated: 07/03/2022
#
#
#
######################################

from DataBaseMethods import dataBaseMethods
from dataHelperFunctions import databaseHelpers
from flask import Flask, request, render_template  
from SunLightAlgorithm import SunLightAlgorithm

helper = databaseHelpers()
dbMethods = dataBaseMethods()
sunLightAlgorithm = SunLightAlgorithm()

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        electricity_bill = request.form['electricity_bill']
        date = request.form['date']
    # strip zip code in date to have no extra spaces
    zipCode = str(zipcode).strip()
    date = str(date).strip()
    
    # get the latitude and longitude 
    result = dbMethods.getLatLongFromZip(zipCode)
    LongLat = list(result)

    # get a the past week from the day that was given
    weekOfDates = helper.getDaysOfCurrentWeek(date)
    results = []
    for day in weekOfDates:
        result = dbMethods.getEntryFromLonLat(LongLat, day)
        results.append(result)
    
    totalSunLight = sunLightAlgorithm.getTotalSunlightForWeek(results)
    return render_template('results.html', variable=totalSunLight, variable2 = results[0])

@app.route('/about')
def about():
    return render_template("about.html")

def main():
    dbMethods.closeDataBase()

if __name__ == "__main__":
    app.run(debug=True)
    main()
