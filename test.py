import testsum as sm
import pyrebase #import firebase library


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



userid=769246233
day_id=20230629
ses_id="-NZ49YddVofmSrNd4yVM"
sm.summary(db,userid,day_id,ses_id)