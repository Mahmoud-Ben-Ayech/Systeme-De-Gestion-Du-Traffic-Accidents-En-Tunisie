from flask import jsonify
from app.configuration import db_soc

#Fonction de recuperation de tous les donnees de table de BDD 
def get_all_data(table_names):
    myTable1 = db_soc[table_names[0]]
    myTable2 = db_soc[table_names[1]]
    myTable3 = db_soc[table_names[2]]
    return jsonify(list(myTable1.find({}))+list(myTable2.find({}))+list(myTable3.find({})))

#Fonction de recherche via critere specifier dans la table de BDD 
def search_data(data_table_name,choice,critere_recherche):
    myTable=db_soc[data_table_name]
    result=list(myTable.find({critere_recherche:choice}))
    return jsonify(result) 

def getUsers(table_name):
    return list(table_name.find({}))


