"""
The starter code comes with a flask server that serves the website at http://localhost:3000/ 
but also exposes an own API at http://localhost:3000/api/v1/analysis/ accepting a GET request with a JSON object with a single field “uri” 
pointing to an image to analyze.
"""

from flask import Flask, request, jsonify
from analyze import read_image

app = Flask(__name__)

@app.route("/")
def home():
    return "Lab 01"

# API at /api/v1/analysis/ 
@app.route("/api/v1/analysis/", methods=['GET'])
def analysis():
    try:
        get_json = request.get_json()
        image_uri = get_json['uri']
        res = read_image(image_uri)
        return res
    except:
        return jsonify({'error': 'Missing URI in JSON'}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)