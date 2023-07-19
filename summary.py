
#import json
#simport googlemaps

#find  the average of environment temperature
def temp(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum = 0
  a = len(list(data_dict.values()))
  for count in range(0, a - 2):
    sum = sum + list(data_dict.values())[count]["envTemp"]
  result = sum / (a - 2)
  #resultr=round(result,2)
  #print(result)
  db.child("history").child(id).child(date).child(session).update(
    {"envtemp": result})


#find  the average of heartrate
def heart_rate(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum = 0
  a = len(list(data_dict.values()))
  for count in range(0, a - 3):
    sum = sum + list(data_dict.values())[count]["hrtRate"]
  result = sum / (a - 3)
  #resultr=round(result,2)
  #print(result)
  db.child("history").child(id).child(date).child(session).update(
    {"hrtRate": result})


#find  the average of speed
def speed(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum = 0
  a = len(list(data_dict.values()))
  for count in range(0, a - 4):
    sum = sum + list(data_dict.values())[count]["spd"]
  result = sum / (a - 4)
  #resultr=round(result,2)
  #print(result)
  db.child("history").child(id).child(date).child(session).update(
    {"spd": result})


#find  the average of humidity
def humidity(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum = 0
  a = len(list(data_dict.values()))
  for count in range(0, a - 5):
    sum = sum + list(data_dict.values())[count]["hum"]
  result = sum / (a - 5)
  #resultr=round(resultr,2)
  #print(result)
  db.child("history").child(id).child(date).child(session).update({"hum": result})


#find  the average of body temperature
def body_temperature(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum = 0
  a = len(list(data_dict.values()))
  for count in range(0, a - 6):
    sum = sum + list(data_dict.values())[count]["bdyTemp"]
  result = sum / (a - 6)
  #resultr=round(resultr,2)
  #print(result)
  db.child("history").child(id).child(date).child(session).update(
    {"bdyTemp": result})
  

#find  the average of body temperature
def alt(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum = 0
  a = len(list(data_dict.values()))
  for count in range(0, a - 7):
    sum = sum + list(data_dict.values())[count]["alt"]
  result = sum / (a - 7)
  #resultr=round(resultr,2)
  #print(result)
  db.child("history").child(id).child(date).child(session).update(
    {"alt": result})
  
#find  the time duration
def timeduration(db,datetime, id, date, session):
  summary = db.child("history").child(id).child(date).child(session).get()
  result_dict = {}
  for item in summary.each():
    if item.key() == "strt":
      start_time = item.val()
    if item.key() == "stp":
      stop_time = item.val()

  if start_time is not None and stop_time is not None:
    start_time_str = str(start_time).ljust(6, '0')
    stop_time_str = str(stop_time).ljust(6, '0')

    start_time_dt = datetime.strptime(start_time_str, "%H%M%S")
    stop_time_dt = datetime.strptime(stop_time_str, "%H%M%S")

    time_duration = stop_time_dt - start_time_dt
    time_duration_str = str(time_duration)

    # Extract hours, minutes, and seconds from the time duration
    hours, remainder = divmod(time_duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_format = f"{hours:02d}{minutes:02d}{seconds:02d}"
    print(time_format)
    db.child("history").child(id).child(date).child(session).update(
      {"timed": time_format})
    
#Total distance calculator
#def distance_calculator(db,datetime, id, date, session):
  #gmaps = googlemaps.Client(key='AIzaSyDVe_UbuxI4Hw2LO-mfJWQfSKfNFmVYExE')#Map object created
  #To be implemnted
  #get session start lat,long & end lat long each touple eg StartP=(6.7971762, 79.9020273) EndP=(6.7977657, 79.9021842)
  #uncomment bellow 
  #directions_result = gmaps.directions(StartP,EndP) #input should be tuples (6.7971762, 79.9020273) (6.7977657, 79.9021842)
  #directions_result = gmaps.directions((6.7971762, 79.9020273),(6.7977657, 79.9021842))
  #distance = [directions_result[0]['legs'][0]['distance']['text'],directions_result[0]['legs'][0]['start_address'],directions_result[0]['legs'][0]['start_address']]
  #db.child("history").child(id).child(date).child(session).update({"dst": distance[0]})
  #db.child("history").child(id).child(date).child(session).update({"strAd": distance[1]})
  #db.child("history").child(id).child(date).child(session).update({"endAd": distance[2]})


def distance_calculator(googlemaps,db, datetime, id, date, session):
  gmaps = googlemaps.Client(key='AIzaSyDVe_UbuxI4Hw2LO-mfJWQfSKfNFmVYExE')
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()

  subsessions = list(data_dict.values())  # Get the subsessions
  num_subsessions = len(subsessions)

  if num_subsessions > 0:
    # Retrieve latitude and longitude of the first and last subsessions
    start_latitude = subsessions[0]["lat"]
    start_longitude = subsessions[0]["lngT"]
    end_latitude = subsessions[num_subsessions - 10]["lat"]
    end_longitude = subsessions[num_subsessions - 10]["lngT"]

    start_point = (start_latitude, start_longitude)  # Create start point tuple
    end_point = (end_latitude, end_longitude) 
  # Get the start and end points' latitude and longitude
  #start_point = (6.7971762, 79.9020273)
  #end_point = (6.7977657, 79.9021842)

  # Get directions between the start and end points
  directions_result = gmaps.directions(start_point, end_point)

  # Extract distance, start address, and end address from the directions result
  distance = directions_result[0]['legs'][0]['distance']['text']
  start_address = directions_result[0]['legs'][0]['start_address']
  end_address = directions_result[0]['legs'][0]['end_address']

  # Update the database with the distance and addresses
  db.child("history").child(id).child(date).child(session).update(
    {"dst": distance})
  db.child("history").child(id).child(date).child(session).update(
    {"strAd": start_address})
  db.child("history").child(id).child(date).child(session).update(
    {"endAd": end_address})


#add data to the firebase
def summary(googlemaps,datetime,db,id, date, session):
  temp(db,id, date, session)
  heart_rate(db,id, date, session)
  speed(db,id, date, session)
  humidity(db,id, date, session)
  body_temperature(db,id, date, session)
  alt(db,id, date, session)
  timeduration(db,datetime,id, date, session)
  distance_calculator(googlemaps,db, datetime, id, date, session)

 