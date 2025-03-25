from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/coordinates', methods=['GET'])
def coordinates():
    # Your static JSON content
    data = {
        "cameraId": 17,
        "coordinates": [
            {
                "name": "ROI 1",
                "x1": 279,
                "y1": 252,
                "x2": 936,
                "y2": 975
            },
            {
                "name": "ROI 1",
                "x1": 1089,
                "y1": 888,
                "x2": 2529,
                "y2": 1290
            }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    # Listen on all network interfaces so it's accessible globally
    app.run(host='0.0.0.0', port=5000, debug=True)
