#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <ArduinoJson.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00005";

// Node listesi
const String nodeList[] = {"Node01", "Node02", "Node03", "Node04","Node05","Node06","Node07","Node08"}; // Tüm node'ların isimleri
bool receivedFlags[sizeof(nodeList) / sizeof(nodeList[0])];        // Her node için bir flag
StaticJsonDocument<1024> jsonBuffer;                               // Tüm JSON verilerini tutar

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_LOW);
  radio.setChannel(81);
  radio.startListening();

  // Flag'leri sıfırla
  resetFlags();
}

void loop() {
  if (radio.available()) {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);

    // Veriyi ',' ile ayır
    String receivedData = String(text);
    int firstComma = receivedData.indexOf(',');
    int secondComma = receivedData.indexOf(',', firstComma + 1);

    String nodeID = receivedData.substring(0, firstComma);            // Nodeismi
    String sensorType = receivedData.substring(firstComma + 1, secondComma); // Sensor ismi
    int sensorValue = receivedData.substring(secondComma + 1).toInt();       // Değer

    // Node ID'yi kontrol et ve flag'i işaretle
    for (int i = 0; i < sizeof(nodeList) / sizeof(nodeList[0]); i++) {
      if (nodeList[i] == nodeID && !receivedFlags[i]) {
        receivedFlags[i] = true;

        // JSON formatına çevir ve kaydet
        JsonObject sensorData = jsonBuffer.createNestedObject();
        sensorData["sensor_ID"] = nodeID;
        sensorData["sensor_type"] = sensorType;
        sensorData["airQuality"] = sensorValue;

        break;
      }
    }

    if (allNodesReceived()) {
      serializeJson(jsonBuffer, Serial);
      Serial.println();

      resetFlags();
      jsonBuffer.clear();
    }
  }
}


void resetFlags() {
  for (int i = 0; i < sizeof(receivedFlags) / sizeof(receivedFlags[0]); i++) {
    receivedFlags[i] = false;
  }
}

bool allNodesReceived() {
  for (int i = 0; i < sizeof(receivedFlags) / sizeof(receivedFlags[0]); i++) {
    if (!receivedFlags[i]) {
      return false;
    }
  }
  return true;
}