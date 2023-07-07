
#import json

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



#add data to the firebase
def summary(datetime,db,id, date, session):
  temp(db,id, date, session)
  heart_rate(db,id, date, session)
  speed(db,id, date, session)
  humidity(db,id, date, session)
  body_temperature(db,id, date, session)
  alt(db,id, date, session)
  timeduration(db,datetime,id, date, session)


 