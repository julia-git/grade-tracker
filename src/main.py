from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
grades = client.tracker.grades

# d={}
# for _ in range(3):
#     name = str(input("student name:"))
#     klass = str(input("student class:"))
#     grade = float(input("grade:"))
#     print(name, klass, grade)
#     d = {"name": name, "klass": klass, "grade": grade}
#     grades.insert_one(d)

count = grades.find().count()
total = 0
for g in grades.find():
    total += g["grade"]
print(total/count)