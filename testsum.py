#find  the average of environment temperature
def temp(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum=0
  a=len(list(data_dict.values()))
  for count in range (0,a-2):
    sum=sum+list(data_dict.values())[int(count)]["envTemp"]
  result=sum/(a-2)
  print(result)
  #db.child("history").child(id).child(date).child(session).update({"envtemp": result})

#find  the average of heartrate
def heart_rate(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum=0
  a=len(list(data_dict.values()))
  for count in range (0,a-3):
    sum=sum+list(data_dict.values())[int(count)]["hrtRate"]
  result=sum/(a-3)
  print(result)
  #db.child("history").child(id).child(date).child(session).update({"heart rate": result})

  
#find  the average of speed
def speed(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum=0
  a=len(list(data_dict.values()))
  for count in range (0,a-4):
    sum=sum+list(data_dict.values())[int(count)]["spd"]
  result=sum/(a-4)
  print(result)
  #db.child("history").child(id).child(date).child(session).update({"speed": result})

  
#find  the average of humidity
def humidity(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum=0
  a=len(list(data_dict.values()))
  for count in range (0,a-5):
    sum=sum+list(data_dict.values())[int(count)]["hum"]
  result=sum/(a-5)
  print(result)
  #db.child("history").child(id).child(date).child(session).update({"humidity": result})
  
#find  the average of body temperature
def body_temperature(db,id, date, session):
  data = db.child("history").child(id).child(date).child(session).get()
  data_dict = data.val()
  sum=0
  a=len(list(data_dict.values()))
  for count in range (0,a-6):
    sum=sum+list(data_dict.values())[int(count)]["bdyTemp"]
  result=sum/(a-6)
  print(result)
  #db.child("history").child(id).child(date).child(session).update({"body temp": result})


# writes summary
def summary(db,id, date, session):
  #temp(db,id, date, session)
  #heart_rate(db,id, date, session)
  #speed(db,id, date, session)
  humidity(db,id, date, session)
  #body_temperature(db,id, date, session)