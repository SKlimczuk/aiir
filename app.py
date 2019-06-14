import os
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://namidad:Namidad12@triage-su1vl.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["triage"]

mycol = mydb["sizes"]
x = mycol.find_one()

if x["numberOfComputers"] <= 1:
    nodes = str(5)
else:
    nodes = str(x["numberOfComputers"])

if x["sizeOfPopulation"] <= 0:
    sizeOfPopulation = str(10000)
else:
    sizeOfPopulation = str(x["sizeOfPopulation"])

if x["amountOfGeneration"] <= 0:
    amountOfGenerations = str(5)
else:
    amountOfGenerations = str(x["amountOfGeneration"])

os.system("mpiexec -np " + nodes + " -hostfile hostfile python main.py " + sizeOfPopulation + " " + amountOfGenerations)

with open('result', 'r') as f:
    resultList = [line.strip() for line in f]

mycol = mydb["numbers"]
for x in resultList:
    mycol.update({'scoreId': 0}, {'$push': {'score': x}})
