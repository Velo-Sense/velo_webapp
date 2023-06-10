
from flask import Flask, render_template, jsonify
import pyrebase
import database_fun as dbf

from collections import OrderedDict #for creating ordered dictionary

config = {
  "apiKey": "AIzaSyDVe_UbuxI4Hw2LO-mfJWQfSKfNFmVYExE",
  "authDomain": "fir-phoneauth1-1208a.firebaseapp.com",
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/<ss_id>')
def get_data(ss_id):
    query = dbf.session_data(db,"history", "769246233",ss_id)
    response_dict =query.val()
    return jsonify(response_dict)

@app.route('/days')#retrive dates by userid
def get_days():
    query = dbf.retreivedate2(db,"history", "769246233")
    dict_days = OrderedDict()

    for item in query:
        i=0
        dict_days.update({item.key(): {'day': item.val().get("date")}})
    return jsonify(dict_days)

#feed json output on 
@app.route('/session')#retrive session by date
def get_s_by_days():
    query = dbf.session_by_date(db,"history", "769246233")
    dict_days = OrderedDict()

    for item in query:
        i=0
        dict_days.update({item.key(): {'day': item.val().get("date")}})
    return jsonify(dict_days)

#feed json output on function to retrive subsessions (func 1)
@app.route('/subsessions')
def retreivesubsessions():
    query = dbf.retreivesubsessions(db,"history", "769246233", "20230523", "1")
    return jsonify(query) 
    

#feed json output on function to retrive only date by given id(func 3)
@app.route('/date')
def retreivedate():
    query = dbf.retreivedate(db,"history", "769246233")
    return jsonify(query)
    
    
#feed json output on  function to retrive only time by given date(func 4)
@app.route('/time')
def  retrieve_sessions_with_time():
    query = dbf. retrieve_sessions_with_time(db,"history", "769246233", "20230524")
    return jsonify(query)
   

 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)