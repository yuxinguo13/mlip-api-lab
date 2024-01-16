from flask import Flask, request, jsonify
from analyze import read_image

app = Flask(__name__)

@app.route("/")
def home():
    image_uri = "https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/raw/master/samples/vision/images/make_things_happen.jpg"
    res = read_image(image_uri)
    return res

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
