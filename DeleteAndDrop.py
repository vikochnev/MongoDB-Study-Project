# Running this file will delete entries and drop DB
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb"]
mycol = mydb["people"]


# delete single query by address
myquery = {"address": "Mountain 21"}
x = mycol.delete_one(myquery)
print(x.deleted_count, " documents deleted.")


# delete multiple entries
myquery = {"address": {"$regex": "^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")


# delete all remaining entries
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")


# drop collection
mycol.drop()