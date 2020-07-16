from pymongo import MongoClient
from settings import DB_HOSTS, DB_PORT, DB_PWD, DB_USERNAME

client = MongoClient(DB_HOSTS, DB_PORT)
db = client.Bandou
db.authenticate(DB_USERNAME, DB_PWD)
