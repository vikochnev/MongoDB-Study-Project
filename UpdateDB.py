# Running this file will update DB entries

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb"]
mycol = mydb["people"]


# Updating single entry
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)
print("Updating single entry: ")
print(mycol.find_one({"address": "Canyon 123"}), "\n\n")


# Updating multiple entries
myquery = {"address": { "$regex": "^S" }}
newvalues = {"$set": { "address": "Funny st 137"}}
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
print('Residents with "Funny st 137" address:')
myquery = {"address": "Funny st 137"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

print("\n\n")