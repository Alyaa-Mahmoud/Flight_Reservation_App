import sqlite3

#create database and connect
def init_database():
    db = sqlite3.connect('flights.db')
    # setting up cursur
    cr = db.cursor()
    # create tables and fields
    cr.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
        flight_number INTEGER,
        name TEXT,
        departure TEXT  ,
        destination TEXT,
        date INTEGER,
        seat TEXT
        )
        ''')
    # save changes
    db.commit()
    # close database
    db.close()
        

        

    



