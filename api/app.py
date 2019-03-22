from flask import Flask, request, jsonify
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route("/predict",methods=["GET"])
def predict_acceptance_rate():
    data=request.json
    keys=data.keys()
    required=["GRE Score","TOEFL Score","CGPA","University Rating","SOP"]
    for i in required:
        if i not in keys:
            message="Please include all the data"
            return jsonify(message=message),200
    a=[ j for i,j in data.items()]
    b=[]
    b.append(a)
    x=model.predict(b)
    return jsonify(acceptance=x[0])

if __name__=="__main__":
    model=joblib.load("usa-graduate-admission.pkl")
    app.run()