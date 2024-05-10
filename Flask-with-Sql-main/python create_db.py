import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create a cursor object
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS registrations
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              email TEXT UNIQUE,
              password TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()
