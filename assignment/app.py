
from flask import Flask, jsonify, request, render_template, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'my_secret_key'

users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    'users4': 'password4'
}
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/gallery')
def home():
    return render_template('gallery.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome to the Home Page!</h1>'
        else:
            return '<h1>Invalid Credentials. Please try again.</h1>'
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
        