import os
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://namidad:Namidad12@triage-su1vl.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["triage"]

mycol = mydb["sizes"]
x = mycol.find_one()

nodes = '5'

if x["sizeOfPopulation"] <= 0:
    sizeOfPopulation = 10000
else:
    sizeOfPopulation = str(x["sizeOfPopulation"])

amountOfGenerations = '5'

os.system("mpiexec -np " + nodes + " -hostfile hostfile python main.py " + sizeOfPopulation + " " + amountOfGenerations)

with open('result', 'r') as f:
    resultList = [line.strip() for line in f]

mycol = mydb["numbers"]
for x in resultList:
    mycol.update({'scoreId': 0}, {'$push': {'score': x}})

def update_tags(new_score):
    coll.update({'scoreId': 0}, {'$push': {'score': new_score}})