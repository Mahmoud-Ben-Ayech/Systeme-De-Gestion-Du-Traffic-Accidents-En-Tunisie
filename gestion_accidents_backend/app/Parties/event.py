from flask import request
from app import app
from app.shared_functions import get_all_data
from flask import jsonify
from app.configuration import table_user

#Event

event_table_name=['Event','twitter','userData']

@app.route('/Event/getAll')
def getAllEvent():
    return get_all_data(event_table_name)

@app.route('/Event/postEvent', methods=['POST'])
def add_event():
    list_ids=table_user.distinct('_id')
    if len(list_ids) >= 1 : 
        last_id=max(list_ids)
    else :
        last_id=0    
    Titre=request.json['titre']
    Evenement=request.json['evenement']
    Date=request.json['date']
    if Titre!='' and Evenement!='' and Date!='' :
        table_user.insert_one({'_id':last_id+1,'Titre':Titre,'Evenement':Evenement,'Date':Date})
        return jsonify({"succes":"addition successfully ! "}) , 200
    return jsonify({"error":"empty elements was detected !"}) 




