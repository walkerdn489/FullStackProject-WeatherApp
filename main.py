
import sqlite3
#from flask import Flask

#app = Flask(__name__)

con = sqlite3.connect('DatabaseName.db')
cur = con.cursor()

#def addUser(email, username):

    # Insert a row of data
#    cur.execute("INSERT INTO testTable VALUES (?, ?)", (email, username))

    # Save (commit) the changes
#    con.commit()

#@app.route('/')
#def hello():
#    return '<h1>Hello, World!</h1>'

def main():
    pass

if __name__ == "__main__":
    main()