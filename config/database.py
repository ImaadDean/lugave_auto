from pymongo import MongoClient

client = MongoClient("mongodb+srv://imaad:Ertdfgxc@cluster0.mnlujl0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.lugave_auto_db

# Collections
car_collection = db["Car"]
user_collection = db["User"]
sale_collection = db["Sale"]
payment_collection = db["Payment"]
payment_schedule_collection = db["Payment_Schedule"]
customer_collection = db["Customer"]
expense_collection = db["Expense"]
