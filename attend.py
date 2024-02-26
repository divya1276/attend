from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create the database and table
def create_table():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attendance
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, event TEXT, attendee TEXT, status TEXT)''')
    conn.commit()
    conn.close()

# Route to render the form for marking attendance
@app.route('/')
def index():
    return render_template('index10.html')

# Route to handle marking attendance
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    event = request.form['event']
    attendee = request.form['attendee']
    status = request.form['status']
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("INSERT INTO attendance (event, attendee, status) VALUES (?, ?, ?)", (event, attendee, status))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to display attendance records
@app.route('/attendance_records')
def attendance_records():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM attendance")
    records = c.fetchall()
    conn.close()
    return render_template('attendance_records.html', records=records)

if __name__ == '__main__':
    create_table()
    app.run(debug=True,port=50023)
