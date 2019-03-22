from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

@app.route("/predict",methods=["GET"])
def predict_acceptance_rate():
    pass

if __name__=="__main__":
    model=joblib.load("usa-graduate-admission.pkl")
    app.run(host="127.0.0.1",port=8080)