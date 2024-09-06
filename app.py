# importing SQLite Module
import sqlite3 
# Connect to SQLite database or create it if it the database doesn't exist. 
conn = sqlite3.connect('Sample.db') 
cursor = conn.cursor() 
# Creating a Sample table.
cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, FirstName TEXT, LastName Text, Age INTEGER, Course varchar)''') 
# Inserting a record. 
cursor.execute("INSERT INTO students (FirstName,LastName,Age,Course) VALUES (?, ?, ?, ?)", ('Venkat Sai','Emani',22,"Computer Science")) 
# Commit the changes.
conn.commit()
# Query the database.
cursor.execute("SELECT * FROM students") 
# Retrieving all rows from the query result.
rows = cursor.fetchall() 
# print the records in the terminal. 
for row in rows: 
 print(row)
# Closing the connection.
conn.close()