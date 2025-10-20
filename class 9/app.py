from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS members (name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO members (name, email, city, country, phone) VALUES (?, ?, ?, ?, ?)',
                       (name, email, city, country, phone))
        conn.commit()
       
        return redirect(url_for('index'))
    else:
        return render_template('join.html')
    
@app.route('/participants')
def participants():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM MEMBERS')
    data = cursor.fetchall()
    connect.close()
    return render_template('participants.html', data=data)

if __name__ == '__main__':
    app.run()