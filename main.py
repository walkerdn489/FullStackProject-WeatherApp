
import sqlite3
from flask import Flask, render_template      

app = Flask(__name__)

con = sqlite3.connect('SolarDatbase.db')
cur = con.cursor()

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")


#def addUser(email, username):

    # Insert a row of data
#    cur.execute("INSERT INTO testTable VALUES (?, ?)", (email, username))

    # Save (commit) the changes
#    con.commit()

#def main():
#    pass

if __name__ == "__main__":
    app.run(debug=True)