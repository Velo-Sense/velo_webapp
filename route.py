from flask import Flask, render_template,jsonify
import os
import pyrebase #import firebase library
import database_fun as dbf
from flask_cors import CORS

config = {
  "apiKey": "AIzaSyDVe_UbuxI4Hw2LO-mfJWQfSKfNFmVYExE",
  "authDomain": "matheesha.me",
  "databaseURL":
  "https://fir-phoneauth1-1208a-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "fir-phoneauth1-1208a",
  "storageBucket": "fir-phoneauth1-1208a.appspot.com",
  "messagingSenderId": "57907367912",
  "appId": "1:57907367912:web:8812c804b2108d11701e5d",
  "measurementId": "G-8VFK1RBCET"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()



app = Flask(__name__)
app.static_folder = 'static'
CORS(app)

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/dashboard')
def symbol():
    return render_template('dashboard.html', the_title='Tiger As Symbol')

@app.route('/history')
def myth():

    test1=""
    #print(test['alt'])
    return render_template('history.html', name=test1)


#------------------Json Data Feeders---------#

#-session data feeder----#
@app.route('/data/<ss_id>')
def get_data(ss_id):

    data = {
        'name': 'John',
        'age': ss_id,
        'city': 'New York'
    }
    return jsonify(data)

#

#-By session date feeder--#


#--Test Feeder------#
@app.route('/testfeed')
def get_test_data():
    data = {1:{1:{'alt':50,'text':80},2:{'alt':87,'text':7},3:{'alt':86,'text':7},4:{'alt':87,'text':7},5:{'alt':81,'text':78},6:{'alt':8,'text':76},7:{'alt':2,'text':76}}}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
