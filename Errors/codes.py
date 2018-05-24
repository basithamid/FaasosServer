import json
def invalidRequestMethod():
    return json.dumps({"status": 405, "message": { "data": "Invalid Method" }})

def invalidData():
    return json.dumps({"status": 406, "message": { "data": "Wrong data passed" }})

def genericException():
    return json.dumps({"status": 500, "message": { "data": "There was some error"}})