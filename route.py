from flask import Flask, render_template,jsonify,request,redirect, url_for
import os
import pyrebase #import firebase library
import database_fun as dbf
from flask_cors import CORS
import summary as sm

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
app.config['userid'] =''#store userid here phone no eg 769246233
app.config['day_id'] ='20230524'#store day_id here eg 20230524
app.config['ses_id'] ='1'#store session id here eg 1
CORS(app)

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/dashboard')
def symbol():
    return render_template('dashboard.html', the_title='Tiger As Symbol')

@app.route('/history', methods=['POST'])
def myth():
    ss_date = str(request.form.get('button'))
    app.config['day_id']=ss_date
    test3=app.config['userid']+'/'+app.config['day_id']
    #print(test['alt'])
    return render_template('history.html', value=test3)


@app.route('/day')
def day():

    test1=app.config['userid']
    #print(test['alt'])
    return render_template('date.html', value=test1)

@app.route('/session', methods=['POST'])
def session():
    ss_id = str(request.form.get('button'))
    app.config['ses_id']=ss_id
    test1=app.config['userid']+'/'+app.config['day_id']+'/'+app.config['ses_id']
    #print(test['alt'])
    return render_template('interface.html', value=test1)


@app.route('/process', methods=['POST'])
def process_form():
    userid = request.form.get('number')
    app.config['userid'] = userid #store userid obtained from the form 
    return redirect('/day')



#2023-06-15 Test form for maleesha
@app.route('/process2', methods=['POST'])
def process2_form():
    #userid=55
    userid = request.form.get('route')
    return f"Ashan"

# Load Browser Favorite Icon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='image/favicon.ico')



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


#-By session date feeder--#


 #feed json output on function to retrive subsessions (func 1)
@app.route('/<user>/<date>/<session>')
def retreivesubsessions(user,date,session):
    query = dbf.retreivesubsessions(db,"history",user,date,session)
    return jsonify(query) 
    

#feed json output on function to retrive only date by given id(func 3)
@app.route('/<user>')
def retreivedate(user):
    query = dbf.retreivedate(db,"history",user)
    return jsonify(query)
    
    
#feed json output on  function to retrive only time by given date(func 4)
@app.route('/<user>/<date>')
def  retrieve_sessions_with_time(user,date):
    query = dbf. retrieve_sessions_with_time(db,"history",user,date)
    return jsonify(query)
    
@app.route('/testfeed')
def get_test_data():
    data = {1:{1:{'alt':50,'text':80,'long':79.901136,'lang':6.794835},2:{'alt':87,'text':7,'long':79.901136,'lang':6.794835},3:{'alt':86,'text':7,'long':79.902431,'lang':6.794499},4:{'alt':87,'text':7,'long':79.902767,'lang':6.794816},5:{'alt':81,'text':78,'long':79.903120,'lang':6.795221},6:{'alt':8,'text':76,'long':79.903557,'lang':6.795344},7:{'alt':2,'text':76,'long':79.903965,'lang':6.795107}}}
    return jsonify(data)

 
 
@app.route('/testfeed5')
def get_test_data2():
    data = {1:{'alt':50,'text':80,'long':79.901136,'lang':6.794835},2:{'alt':87,'text':7,'long':79.901136,'lang':6.794835},3:{'alt':86,'text':7,'long':79.902431,'lang':6.794499},4:{'alt':87,'text':7,'long':79.902767,'lang':6.794816},5:{'alt':81,'text':78,'long':79.903120,'lang':6.795221},6:{'alt':8,'text':76,'long':79.903557,'lang':6.795344},7:{'alt':2,'text':76,'long':79.903965,'lang':6.795107}}
    return jsonify(data)

#6.794835, 79.901136
#6.794835, 79.901136
#6.794499, 79.902431
#6.794816, 79.902767
#6.795221, 79.903120
#6.795344, 79.903557
#6.795107, 79.903965

#------------Sumarization function--------#

#https://reqbin.com/ API Test platform
#{"uid":"769246233","date":"20230630","ses":"-NZ9yhXn5LvvNGsRiCOb"}
#
@app.route('/summary',methods=['POST'])
def summarizer():
    #user="769246233"
    #date="20230630"
    #session="-NZ9yhXn5LvvNGsRiCOb"
    user = str(request.form.get('uid'))
    date=str(request.form.get('date'))
    session=str(request.form.get('ses'))
    sm.summary(db,user,date,session)
    return f"OK"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
