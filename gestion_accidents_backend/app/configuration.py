import pymongo

client=pymongo.MongoClient('localhost',27017)
db_soc = client["db_soc"]
table_site = db_soc["Event"]

table_twit=db_soc["twitter"]

table_user=db_soc["userData"]

collection_users=db_soc["User"]




