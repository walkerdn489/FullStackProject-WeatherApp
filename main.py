
import sqlite3
con = sqlite3.connect('DatabaseName.db')
cur = con.cursor()

def addUser(email, username):

    # Insert a row of data
    cur.execute("INSERT INTO testTable VALUES (?, ?)", (email, username))

    # Save (commit) the changes
    con.commit()

def main():

    email = input("Email: ")
    username = input("Username: ")

    addUser(email,username)

    for row in cur.execute('SELECT email, username FROM testTable'):
        print(row)


if __name__ == "__main__":
    main()