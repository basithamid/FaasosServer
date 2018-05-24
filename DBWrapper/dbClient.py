from pymongo import MongoClient
from bson.json_util import dumps
from Errors import codes
import json

class MongoDatabase:

    def __init__(self, host, port):
        client = MongoClient(host = host, port = port)
        self.db = client.faasosDB

    def getExistingDishes(self):
        try:
            ordersdb = self.db.orders
            records = dumps(ordersdb.find({}, {'name':1, '_id': 0}))
            records = json.loads(records)
            return json.dumps({"status": 200 , "message":{ "data": records }})
        except:
            return codes.genericException()

    def getOrders(self):
        try:
            ordersdb = self.db.orders
            records = dumps(ordersdb.find({}, {'_id': 0}))
            records = json.loads(records)
            return json.dumps({"status": 200, "message": {"data": records}})
        except:
            return codes.genericException()

    def placeOrder(self, data):
        ordersdb = self.db.orders
        try:
            if 'dish' in data and 'quantity' in data:
                record = dumps(ordersdb.find_one({'name': data['dish']}, {'quantity': 1, '_id': 0}))
                record = json.loads(record)
                json.dumps(ordersdb.update({'name': data['dish']},
                                           {'$set': {'quantity': data['quantity'] + record['quantity']}}))
                return json.dumps({"status":200, "message": {"data": "Order Placed"}})
            else:
                return codes.invalidData()
        except:
            return codes.genericException()

    def predictOrders(self, data):
        ordersdb = self.db.orders
        try:
            if 'dish' in data and 'quantity' in data:
                json.dumps(ordersdb.update({'name': data['dish']},
                                           {'$set': {'predicted': data['quantity']}}))
                return json.dumps({"status": 200, "message": {"data": "Prediction completed"}})
            else:
                return codes.invalidData()
        except:
            return codes.genericException()

    def update(self, data):
        ordersdb = self.db.orders
        try:
            if 'name' in data and 'quantity' in data and 'createdTillNow' in data and 'predicted' in data:
                json.dumps(ordersdb.update({'name': data['name']},
                                           {'$set': {'quantity': 0,
                                                     'createdTillNow': data['createdTillNow'] + data['quantity']}}))

                return self.getOrders()
            else:
                return codes.invalidData()
        except:
            return codes.genericException()
