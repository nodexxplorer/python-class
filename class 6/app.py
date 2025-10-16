from flask  import Flask, request, make_response 
app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('cookie Set')
    resp.set_cookie('MITA SCHOOL', 'I MIGHT LIKE PYTHON CLASS')
    return resp

  

@app.route('/get_cookie')
def get_cookie():
    mita_cookie = request.cookies.get('MITA SCHOOL')
    if mita_cookie:
        return 'MITA SCHOOL: ' + mita_cookie
    else:
        return 'NO MITA SCHOOL cookie found'
    
app.run()