from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = '00000'

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Route to add a new student
@app.route('/addstudent')
def new_student():
    return render_template('add_student.html')

# Route to handle the insertion of a new student record
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            # Retrieve form data
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pin']
            
            # Insert data into the database
            with sql.connect("student_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (name, address, city, pin))
                con.commit()
                msg = "Record successfully added!"
        except Exception as e:
            con.rollback()
            msg = f"Error in insert operation: {e}"
        finally:
            con.close()
            return render_template("list.html", msg=msg)

# Route to display the list of students
@app.route('/list')
def list():
    with sql.connect("student_database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        return render_template("list.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)
