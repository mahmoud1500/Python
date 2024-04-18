import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE developers (
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
    
    insert_data = [
        (1,'Jane', 'Alison', 'Jane@ss.com','44444444','123 a sw','lynnwood','WA','98036'),
        (2,'Jack', 'Ibrahim', 'Jack@ss.com','44444445','123 a sw','lynnwood','WA','98036'),
        (3,'Joe', 'Biden', 'joe@ss.com','44444446','123 a sw','lynnwood','WA','98036'),
        (4,'Nick', 'Trump', 'Nick@ss.com','44444447','123 a sw','lynnwood','WA','98036'),
        (5,'Zack', 'Tomas', 'Zack@ss.com','44444448','123 a sw','lynnwood','WA','98036'),
        (6,'Cherry', 'Allen', 'Cherry@ss.com','44444449','123 a sw','lynnwood','WA','98036'),
        (7,'Bon', 'Chi', 'bon@ss.com','4444450','123 a sw','lynnwood','WA','98036'),
        (8,'Soliman', 'Moe', 'soliman@ss.com','44444421','123 a sw','lynnwood','WA','98036'),
        (9,'Kim', 'Soe', 'kim@ss.com','44444451','123 a sw','lynnwood','WA','98036'),
        (10,'Andrea', 'Hoz', 'andrea@ss.com','44444452','123 a sw','lynnwood','WA','98036'),]
    
    for data in insert_data:
        insert_stmt = '''
    INSERT INTO developers (id,firstname,last_name,email_address,phone,street_address,city,state,zip_code)
    VALUES (?,?,?,?,?,?,?,?,?)'''     
        cursor.execute(insert_stmt,data)
    
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        
        print("sqlite connection is closed")

def List_Names():
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT firstname,last_name FROM developers ")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close
def ID_ZIP():
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT id,zip_code FROM developers")
    results = cursor.fetchall()
    for row in results:
        print (row)

def email_state():
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT email_address,state FROM developers")
    results = cursor.fetchall()
    for row in results:
        print (row)

List_Names()
ID_ZIP()
email_state()