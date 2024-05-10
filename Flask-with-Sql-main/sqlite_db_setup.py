import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Opened database successfully at {db_file}")
    except Exception as e:
        print(f"Error connecting to database at {db_file}: {e}")
    return conn

def create_student_table(conn):
    """Create a student table if it does not exist already."""
    try:
        cur = conn.cursor()
        # Ensure the SQL statement is on one line if encountering operational errors
        cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, address TEXT NOT NULL, city TEXT NOT NULL, pin TEXT NOT NULL)')
        print("Student table created successfully")
    except Exception as e:
        print(f"Error creating student table: {e}")

def main():
    database = "student_database.db"

    # Create a database connection
    conn = create_connection(database)

    # Create student table
    if conn is not None:
        create_student_table(conn)
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()







