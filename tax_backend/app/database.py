from pymongo import MongoClient
from config import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client.taxDB  # Database name
users_collection = db.users
tax_data_collection = db.tax_data
