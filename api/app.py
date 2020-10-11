from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/predict",methods = ["GET"])
def predict_acceptance_rate():
	if request.method == "GET":
		if 'gre' in request.args and 'toefl' in request.args and 'cgpa' in request.args and 'unirating' in request.args and 'sop' in request.args:
			gre = int(request.args['gre'])
			if gre < 160 or gre > 340:
				message = "GRE score cannot be more than 340 or less than 160"
				return jsonify(message = message),200
			toefl = int(request.args['toefl'])
			if toefl <= 0 or toefl > 120:
				message = "TOEFL score cannot be more than 120 or less than 0"
				return jsonify(message = message),200
			cgpa = int(request.args['cgpa'])
			if cgpa > 10:
				message = "CGPA cannot be more than 10"
				return jsonify(message = message),200
			unirating = int(request.args['unirating'])
			if unirating > 5 or unirating < 1:
				message = "Unirating between 1-5"
				return jsonify(message = message),200
			sop = int(request.args['sop'])
			if sop > 5 or sop < 1:
				message = "SOP rating b/w 1-5"
				return jsonify(message = message),200
			data = [gre, toefl, cgpa, unirating, sop]
		else:
			message = "Please include all the data"
			return jsonify(message = message),200
	else:
		message = "Please send data after url"
		return jsonify(message = message),200

	x = model.predict([data])
	return jsonify(acceptance = x[0])

if __name__ == "__main__":
	file = open("usa-graduate-admission2.sav","rb")
	model = pickle.load(file)
	app.run()
