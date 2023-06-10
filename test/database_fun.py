#---Retrieve data from firebase by given session----Sachini
def session_data(db,table, id, date):
  summary = db.child(table).child(id).child(date).get()
  return summary

#---Retrieve data from Phonenum ----Sachini
def retreivedate2(db,table, id):
  summary = db.child(table).child(id).get()
  return summary

#---Retrieve data from firebase by given session----Sachini
def session_by_date(db,table, id, date):
  summary = db.child(table).child(id).child(date).get()
  return summary
  
  
#function to retrive subsessions (func 1)----Sachini
def retreivesubsessions(db,table, id, date, session):
  summary = db.child(table).child(id).child(date).child(session).get()
  result_dict = {}

  for item in summary:
    result_dict[item.key()] = item.val()
  print(result_dict)

  return result_dict
  
  
#function to retrive only date by given id(func 3)----Sachini
def retreivedate(db,table, id):
  summary = db.child(table).child(id).get()
  result_dict = {}

  for item in summary:
    result_dict[item.key()] = item.val().get("date")
  print(result_dict)

  return result_dict
  

 #function to retrive only time by given date(func 4)----Sachini
def retrieve_sessions_with_time(db,table, id, date):
  sessions = db.child(table).child(id).child(date).get()
  result_dict = {}

  for session in sessions.each():
    if "time" in session.val():
      result_dict[session.key()] = session.val()["time"]

  print(result_dict)

  return result_dict