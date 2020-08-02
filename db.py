import pymongo

from datetime import datetime  

# Connect to database
mongoURL = "mongodb+srv://bash:bash123@cluster0-ucvae.mongodb.net/test?retryWrites=true&w=majority"

mongoClient = pymongo.MongoClient(mongoURL)
database = mongoClient["expense_manager"]
collection = database["expenses"]
user_settings = database["settings"]

print('DB: Connection initiated...')

def insert_record(name, expense, category, date):
    dateString = date.strftime('%Y%m%d')
    record = {"name": name, "amount": int(expense), "category": category, "date": dateString, "timestamp": date}
    collection.insert_one(record)
    print('DB: Inserted Record: ', record)

def get_records_by_date(date):
    findDate = date.strftime('%Y%m%d')
    print('DB: Fetching Records by Date: ', findDate)
    records = list(collection.find({"date": findDate}))
    print('DB: Fetching Records Complete')
    return records

def get_all_records():
    print('DB: Fetching Records...')
    records = list(collection.find())
    print('DB: Fetching Records Complete')
    return records

def delete_record(idx):
    deletionQuery = {'_id': idx}
    record = collection.delete_one(deletionQuery)
    print('DB: Deleted Record: ', record)

def edit_record(id, name, amount, category):
    editQuery = { "_id": id }
    newRecord = { "$set": { "name": name, "amount": int(amount), "category": category } }

    collection.update_one(editQuery, newRecord)
    print('DB: Edited Record to: ', newRecord)

def sort_record_date():
    newRecords = collection.find().sort("date")
    return newRecords

def sum_by_day():
    pipeline = [
        {"$group": {"_id": "$date", "total": {"$sum": "$amount"}}},

        # Sort by date
        {"$sort": {"_id": 1}}
    ]
    return list(collection.aggregate(pipeline))

def sum_by_category():
    pipeline = [
        {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
    ]
    return list(collection.aggregate(pipeline))

def get_sum_of_day(date):
    findDate = date.strftime('%Y%m%d')
    pipeline = [
        {"$match": {"date": findDate}},
        {"$group": {"_id": findDate, "total": {"$sum": "$amount"}}}
    ]
    return list(collection.aggregate(pipeline))

def change_settings(theme, dailyLimit, email):
    userId = {"_id": 1}
    settingsValues = {"$set": {"theme": theme, "dailyLimit": dailyLimit, "email": email}}
    user_settings.update_one(userId, settingsValues)
    print('DB: Changed Settings: ', settingsValues)

def get_settings():
    print('DB: Fetching Settings...')
    records = list(user_settings.find())
    print('DB: Fetching Settings Complete')
    return records

# close connection
mongoClient.close()
print('DB: Connection Closed')

