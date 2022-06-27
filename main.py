######################################
# Main function for project 
# Last Updated: 06/26/2022
#
#
#
######################################

from databaseEntry import databaseEntry
from dataHelperFunctions import databaseHelpers

from flask import Flask, request, render_template      

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        electricity_bill = request.form['electricity_bill']
        time = request.form['date']

    helper = databaseHelpers()
    zipCode = str(zipcode).strip()
    time = str(time).strip()
    time = helper.convertDateToTime(time)
    result = helper.getLatLongFromZip(zipCode)
    LongLat = list(result)
    results = helper.getEntryFromLonLat(LongLat, time)

    return render_template('results.html', variable=results)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)