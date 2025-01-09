from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

data_points = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    global data_points
    data = request.get_json()
    sensor_ID = data.get("sensor_ID")
    sensor_type = data.get("sensor_type")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    air_quality = data.get("airQuality")

    if not sensor_ID or not sensor_type or not latitude or not longitude or not air_quality:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    data_points.append({
        "sensor_ID": sensor_ID,
        "sensor_type": sensor_type,
        "latitude": latitude,
        "longitude": longitude,
        "value": air_quality
    })

    socketio.emit('update_map', {
        "sensor_ID": sensor_ID,
        "sensor_type": sensor_type,
        "latitude": latitude,
        "longitude": longitude,
        "value": air_quality
    })

    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5001, debug=True, allow_unsafe_werkzeug=True)