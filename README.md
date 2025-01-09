```markdown
# 🌐 SensorNetworks-25

This project implements a **star topology wireless sensor network (WSN)** using multiple Arduino-based nodes equipped with **MQ135 air quality sensors**. The system collects air quality data from various locations and visualizes it on a real-time map through a web interface.

---

## 📂 Project Structure

```plaintext
SensorNetworks-25/
├── app.py                 # Flask application for serving the web interface and processing data
├── json_sender.py         # Sends data from `sensor_data.json` to the Flask application
├── README.md              # Project documentation
├── sensor_data.json       # Stores sample JSON data for testing
├── serial_port_read.py    # Reads data from the sink node via serial communication
│
├── NodeCode/
│   ├── Node1/
│   │   └── Node1.ino      # Arduino code for a sensor node (reused for all nodes)
│   └── SinkNode/
│       └── SinkNode.ino   # Arduino code for the sink node
│
├── static/
│   ├── heatmap.min.js     # Heatmap library for visualizing data
│   ├── leaflet.css        # Leaflet CSS for map rendering
│   ├── leaflet.js         # Leaflet JavaScript library for map functionality
│   └── technology.png     # Icon or image used in the project
│
└── templates/
    └── index.html         # HTML template for the Flask web interface
```

---

## 🌟 System Overview

This system is designed to monitor air quality across multiple locations using **Arduino-based sensor nodes** equipped with **MQ135 sensors**. The nodes send data to a central **sink node** using **nRF24L01 RF modules**. The sink node aggregates the data and forwards it to a **Flask-based web server**, which visualizes the air quality data on a real-time map.

---

## ✨ Features

- **📡 Real-Time Data Collection**: Sensor nodes continuously monitor air quality and send data to the sink node.
- **🕸️ Star Topology Network**: Efficient communication using a star topology.
- **🌍 Web-Based Visualization**: Displays data on a geographical map using Leaflet and Heatmap.js.
- **🔧 Scalability**: Easily add or remove nodes with minor configuration updates.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Arduino IDE
- Python 3.x
- Flask, Flask-SocketIO, Requests library

### 🛠️ Hardware Requirements

- Multiple Arduino boards (e.g., Arduino Uno)
- MQ135 air quality sensors
- nRF24L01 RF modules for wireless communication

---

## 📝 Setup Instructions

### 1️⃣ Arduino Setup
1. Upload the code from `NodeCode/Node1/Node1.ino` to each sensor node, ensuring **unique identifiers** for each node.
2. Upload the code from `NodeCode/SinkNode/SinkNode.ino` to the **sink node**.

### 2️⃣ Python Environment
1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install the required Python packages:
   ```bash
   pip install flask flask-socketio requests
   ```

### 3️⃣ Run the Flask Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to: [http://127.0.0.1:5001](http://127.0.0.1:5001).

### 4️⃣ Simulate Data Transmission
- Use `json_sender.py` to send sample data without hardware:
  ```bash
  python json_sender.py
  ```

### 5️⃣ Real Hardware Data
- Use `serial_port_read.py` to read data from the sink node via serial communication and forward it to the Flask application.

---

## 🖼️ Visualization

The web interface provides a real-time map visualization of air quality metrics. The markers on the map show:
- **Sensor ID**: The unique identifier of the node.
- **Sensor Type**: Type of the air quality sensor (e.g., MQ135).
- **Air Quality Value**: The measured air quality index (AQI).

### Example Real-Time Map:
![Real-Time Map Example](static/technology.png)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the code or documentation, and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📸 Screenshots
<p align="center">
  <img src="https://github.com/user-attachments/assets/4c0133e5-0852-499b-b00a-78628e119f8b" width="800"/>
</p>

### 🌍 Real-Time Map Interface
![Real-Time Map](https://via.placeholder.com/800x400?text=Real-Time+Map+Example)

### 🖥️ System Architecture
![System Architecture](https://via.placeholder.com/800x400?text=System+Architecture+Diagram)
```


