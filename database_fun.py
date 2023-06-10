#---Retrieve data from firebase by given session----Sachini
def session_data(db,table, id, date):
  summary = db.child(table).child(id).child(date).get()
  return summary

#---Retrieve data from Phonenum ----Sachini
def retreivedate2(db,table, id):
  summary = db.child(table).child(id).get()
  return summary