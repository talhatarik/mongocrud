#!/usr/bin/env python
#coding: utf8 

import Mongo



Mongo.Select("databaseName", "collectionName", "request")

Mongo.Update("databaseName","collectionName", "request")

Mongo.DropCollection("databaseName", "collectionName")

Mongo.DeleteMany("databaseName", "collectionName", "request")


# etc