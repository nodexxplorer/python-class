from flask import Flask, render_template, make_response, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def Login():
    return render_template('login.html')

@app.route('/details', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        output = 'Hi, Welcome ' + name
        resp = make_response(output)
        resp.set_cookie('username', name)
        return resp
    else: 
        return "Mr uwem wan kill me"

app.run()