import serial
import json

ser = serial.Serial('COM4', 9600, timeout=1) 
json_file = "sensor_data.json"

def update_json_file(new_data):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    for sensor in new_data:
        for existing_sensor in data:
            if existing_sensor["sensor_ID"] == sensor["sensor_ID"]:
                data.remove(existing_sensor)
        data.append(sensor)
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Yeni veri: {line}")
                
                parts = line.split(',')
                if len(parts) == 3:
                    node_id = parts[0]         # "Node04"
                    sensor_type = parts[1]    # "MQ4"
                    air_quality = int(parts[2])  # "24"

                    new_data = [{
                        "sensor_ID": node_id,
                        "sensor_type": sensor_type,
                        "airQuality": air_quality
                    }]

                    update_json_file(new_data)
                else:
                    print("Geçersiz veri formatı!")
    except Exception as e:
        print(f"Hata: {e}")
        break