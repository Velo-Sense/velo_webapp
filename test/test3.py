import pyrebase

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

#create user sessions
db.child("users").child("0717223652").update({
  "dob": "2517",
  "email": "anuradha123@gmail.com",
  "phone": "0717223652",
  "name": "Anuradha"
})