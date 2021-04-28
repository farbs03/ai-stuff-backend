from werkzeug.utils import cached_property
from flask import Flask, request, jsonify, make_response
import summarizer
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
port = int(os.environ.get('PORT', 5000))

@app.route('/summarize', methods=['POST'])
@cross_origin()
def summarize():
	response = request.json
	if(request.method == "POST"):
		return jsonify({
			"statusCode": 200,
			"status": "Success",
			"result": summarizer.getSummary(response)
		})
	else:
		return jsonify({
			"ERROR": "No data found"
		})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port = 5000, debug=True)