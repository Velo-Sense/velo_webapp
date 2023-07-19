import database_fun as dbf
import googlemaps
import pyrebase
from datetime import datetime, timedelta
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


#start_point = (6.7971762, 79.9020273)
#end_point = (6.7977657, 79.9021842)

distance=dbf.distance_calculator(db, datetime,"769246233", "20230630",
                                 "-NZ9xGBOTsTCtM5fIDDS")
print(distance)