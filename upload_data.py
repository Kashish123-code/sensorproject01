import pandas as pd
import json
from pymongo import MongoClient
uri = "mongodb+srv://Kashish:Kashish123@cluster0.buk7tfk.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client = MongoClient(uri)


#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME='waferfault'

df=pd.read_csv("D:\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())
json_record
type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

print(df.head())