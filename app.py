from flask import Flask, request, jsonify, render_template
from analyze import read_image

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template('index.html')


# API at /api/v1/analysis/ 
@app.route("/api/v1/analysis/", methods=['GET'])
def analysis():
    try:
        get_json = request.get_json()
        image_uri = get_json['uri']
        res = read_image(image_uri)

        return jsonify(res), 200
    except:
        return jsonify({'error': 'Missing URI in JSON'}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)