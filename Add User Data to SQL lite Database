import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS developers (
                                id INTEGER PRIMARY KEY,
                                firstname TEXT NOT NULL,
                                last_name text NOT NULL UNIQUE,
                                email_address TEXT NOT NULL,
                                phone INTEGER NOT NULL,
                                street_address TEXT NOT NULL,
                                city TEXT NOT NULL,
                                state TEXT NOT NULL,
                                zip_code INTEGER NOT NUll);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        
        print("sqlite connection is closed")

def populate_user():
    for _ in range(5):
        add_user()

def List_Names():
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT * FROM developers ")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close


def add_user():
    firstname = input("What's your First Name : ")
    last_name = input("What's your Last Name : ")
    email_address  = input("What's your Email Adress : ")
    phone  = input("What's your phone Number : ")
    street_address  = input("What's your Stress adress : ")
    city  = input("What's your City : ")
    state  = input("What's your State : ")
    zip_code = input("What's your  Zip code : ")

    cursor = sqliteConnection.cursor()
    insert_stmt = ''' INSERT INTO developers (firstname,last_name,email_address,phone,street_address,city,state,zip_code) 
    VALUES (?,?,?,?,?,?,?,?)'''
    cursor.execute(insert_stmt,(firstname,last_name,email_address,phone,street_address,city,state,zip_code))
    sqliteConnection.commit()
    print("User added successfully")


populate_user()
List_Names()

