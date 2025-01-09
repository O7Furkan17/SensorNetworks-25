# 🌐 SensorNetworks-25

This project implements a **star topology wireless sensor network (WSN)** using multiple Arduino-based nodes equipped with **MQ135 air quality sensors**. The system collects air quality data from various locations and visualizes it on a real-time map through a web interface.

---

## 📂 Project Structure

```plaintext
SensorNetworks-25/
├── NodeCode/
│   ├── Node1/
│   └── SinkNode/
├── static/
├── templates/
├── app.py
├── json_sender.py
├── sensor_data.json
└── serial_port_read.py
```
📁 Directory Details
  NodeCode/:
  Node1/: Code for a sensor node equipped with an MQ135 sensor. This code is reused for other nodes with minor modifications (e.g., unique node identifiers).
  SinkNode/: Code for the sink node responsible for collecting data from all sensor nodes.
  static/: Static files such as CSS and JavaScript for the web interface.
  templates/: HTML templates for the Flask web application.
  app.py: Flask application that serves the web interface and processes incoming data.
  json_sender.py: Python script to read data from sensor_data.json and send it to the Flask application.
  sensor_data.json: Sample JSON data for testing purposes.
  serial_port_read.py: Script to read data from the sink node via the serial port.

🌟 System Overview
The system comprises multiple Arduino-based sensor nodes, each equipped with an MQ135 air quality sensor. These nodes transmit air quality data to a central sink node using RF communication modules (e.g., nRF24L01). The sink node collects the data and forwards it to a Flask-based web server running on a connected computer. The server processes the data and displays it on a real-time map, showing air quality metrics at respective sensor locations.

✨ Features
📡 Real-Time Data Collection: Sensor nodes continuously monitor air quality and transmit data to the sink node.
🕸️ Star Topology Network: Efficient communication between sensor nodes and the sink node.
🌍 Web-Based Visualization: Real-time map interface for geographical visualization of air quality data.
🔧 Scalability: Easily add or remove sensor nodes with minimal configuration.

🚀 Getting Started

✅ Prerequisites
Arduino IDE
Python 3.x
Flask, Flask-SocketIO, Requests library
🛠️ Hardware Requirements
Multiple Arduino boards (e.g., Arduino Uno)
MQ135 air quality sensors
nRF24L01 RF modules for wireless communication

📝 Setup Instructions

1️⃣ Arduino Setup
Upload the code from NodeCode/Node1/ to each sensor node, ensuring each node has a unique identifier.
Upload the code from NodeCode/SinkNode/ to the sink node.

2️⃣ Python Environment
1-Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

2-Install the required Python packages:
    pip install flask flask-socketio requests

3️⃣ Run the Flask Application
Start the Flask server:
    python app.py
    Open your browser and navigate to: http://127.0.0.1:5001.

4️⃣ Simulate Data Transmission
Use json_sender.py to send sample data without hardware:
    python json_sender.py

5️⃣ Real Hardware Data
Use serial_port_read.py to read data from the sink node via serial communication and forward it to the Flask application.

👩🏽‍💻 When the Python files are executed, the data from the sensor is instantly captured, and the values are transmitted to the user and mapped accordingly.
<img src="https://github.com/user-attachments/assets/4c0133e5-0852-499b-b00a-78628e119f8b" width="400"/>

