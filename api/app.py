from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def predict_acceptance_rate():
    data = request.json
    if data == None:
        message = "Please include all the data"
        return jsonify(message = message),200
    keys = data.keys()
    required = ["GRE Score","TOEFL Score","CGPA","University Rating","SOP"]
    for i in required:
        if i not in keys:
            message = "Please include all the data"
            return jsonify(message = message),200
    a = [ j for i,j in data.items()]
    print(a)
    b = [[310,100,8,2,3,5]]
    x = model.predict(b)
    return jsonify(acceptance = x[0])

if __name__ == "__main__":
    file = open("usa-graduate-admission.sav","rb")
    model = pickle.load(file)
    app.run()
