# Running this file makes a few queries which don't change contents of DB/collection

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb"]
mycol = mydb["people"]


# display all entries
print("Display all entries:")

for x in mycol.find():
    print(x)

print("\n\n")


# display entries without their id
print("Display without their id:")

for x in mycol.find({}, {"_id": 0}):
    print(x)

print("\n\n")


# display all entries without name
print("Display excluding name:")
for x in mycol.find({}, {"name": 0}):
    print(x)
print("\n\n")


# filter by specific name
print("Display entries with John:")
mydoc = mycol.find({"name": "John"})
for x in mydoc:
    print(x)

print("\n\n")


# advanced queries:
myquery = {"name": {"$gt": "J"}}
mydoc = mycol.find(myquery)
print("Display entries with names from J to Z:")
for x in mydoc:
    print(x)

print("\n\n")

myquery = {"name": {"$regex": "^S"}}
mydoc = mycol.find(myquery)
print("Display entries with names starting with S:")
for x in mydoc:
    print(x)

print("\n\n")


# sorting by name

mydoc = mycol.find().sort("name")
print("Sorting by name, ascending:")
for x in mydoc:
    print(x)

print("\n\n")

mydoc = mycol.find().sort("name", -1)
print("Sorting by name, descending:")
for x in mydoc:
    print(x)
print("\n\n")


# displaying 1st 5 entries:
myresult = mycol.find().limit(5)
print("Displaying first 5 entries:")
for x in myresult:
  print(x)