import json
import time
import requests

json_file = "sensor_data.json"
api_url = "http://localhost:5001/api/data"
interval = 5

node_locations = {
    "Node01": {"latitude": 38.672784, "longitude": 39.189030}, 
    "Node02": {"latitude": 38.67399119536177, "longitude": 39.18480907769733}, 
    "Node03": {"latitude": 38.674788, "longitude": 39.191657},  
    "Node04": {"latitude": 38.672000, "longitude": 39.189500}, 
    "Node05": {"latitude": 38.672858, "longitude": 39.197168},
    "Node06": {"latitude": 38.677656, "longitude": 39.187802}, 
    "Node07": {"latitude": 38.676878, "longitude": 39.197308},
    "Node08": {"latitude": 38.676676, "longitude": 39.184113}
}

def send_data_from_json():
    while True:
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
            
            for sensor_data in data:
                sensor_id = sensor_data["sensor_ID"]
                location = node_locations.get(sensor_id, {"latitude": 38.672784, "longitude": 39.189030})

                payload = {
                    "sensor_ID": sensor_data["sensor_ID"],
                    "sensor_type": sensor_data["sensor_type"],
                    "latitude": location["latitude"],
                    "longitude": location["longitude"],
                    "airQuality": sensor_data["airQuality"]
                }

                response = requests.post(api_url, json=payload)
                if response.status_code == 200:
                    print(f"Veri başarıyla gönderildi: {payload}")
                else:
                    print(f"Hata: {response.status_code}, {response.json()}")

            time.sleep(interval)

        except Exception as e:
            print(f"Hata: {e}")
            break

if __name__ == "__main__":
    send_data_from_json()