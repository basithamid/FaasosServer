from flask import  Flask, request
from Errors import codes
from DBWrapper import dbClient
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = dbClient.MongoDatabase(host = 'localhost', port = 27017)

@app.route('/getDishes', methods= ['GET'])
def getDishes():
    if request.method == 'POST':
        return codes.invalidRequestMethod()
    else:
        return db.getExistingDishes()

@app.route('/getOrders', methods=['GET'])
def getOrders():
    if request.method == 'POST':
        return codes.invalidRequestMethod()
    else:
        return db.getOrders()

@app.route('/placeOrder', methods=['POST'])
def placeOrder():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        print(request.get_json())
        return db.placeOrder(request.get_json())

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.predictOrders(request.get_json())

@app.route('/updateOrder', methods=['POST'])
def updateOrder():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.update(request.get_json())

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8000)
