from flask import  Flask, request
from Errors import codes
from DBWrapper import dbClient
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
connection_params = {
    'user': 'basit',
    'password': 'root123#',
    'host': 'ds235180.mlab.com',
    'port': 35180,
    'namespace': 'faasos',
}


connection = MongoClient(
    'mongodb://{user}:{password}@{host}:'
    '{port}/{namespace}'.format(**connection_params)
)

db = dbClient.MongoDatabase(connection_params)


@app.route('/getDishes', methods= ['GET', 'POST'])
def getDishes():
    if request.method == 'POST':
        return codes.invalidRequestMethod()
    else:
        return db.getExistingDishes()


@app.route('/getOrders', methods=['GET', 'POST'])
def getOrders():
    if request.method == 'POST':
        return codes.invalidRequestMethod()
    else:
        return db.getOrders()


@app.route('/placeOrder', methods=['POST', 'GET'])
def placeOrder():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.placeOrder(request.get_json())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.predictOrders(request.get_json())


@app.route('/updateOrder', methods=['POST', 'GET'])
def updateOrder():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.update(request.get_json())


@app.route('/')
def index():
    return '<h1>Connected to server.</h1>'

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
