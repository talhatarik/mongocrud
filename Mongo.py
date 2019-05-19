#!/usr/bin/env python
#coding: utf8 
from pymongo import MongoClient #pip3 install pymongo(python3) -veya- pip install pymongo (python2)


address = "localhost"
port = 27017


def InsertOne(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.insert_one(request)


def InsertMany(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.insert_many(request)


def Select(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.find(request)


def Update(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]       
    collection = db[collectionName]
    collection.update_many(request)


def CreateIndex(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]       
    collection = db[collectionName]
    collection.create_index(request)


def Count(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.count(request)


def Aggreate(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.aggreate(request)


def DeleteMany(databaseName, collectionName, request):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.delete_many(request)


def CreateCollection(databaseName, collectionName):
    client = MongoClient(address, port)
    db = client[databaseName]
    db.create_collection(collectionName)


def DropCollection(databaseName, collectionName):
    client = MongoClient(address, port)
    db = client[databaseName]
    collection = db[collectionName]
    collection.drop()

