#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

const byte address[6] = "00005";
const int MQ135_PIN = A0;

char text[32];
int i=0;
int sensorValue = 0;

void setup() {
  radio.begin();
  Serial.begin(9600);
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_LOW);
  radio.setChannel(81);
  radio.stopListening();
}

void loop() {
  sensorValue = analogRead(MQ135_PIN);
  sprintf(text, "Node08,MQ2,%d", sensorValue);
  
  if(radio.write(&text, sizeof(text))){
    Serial.print(text);
    Serial.println("Gonderdi");
  }else {
    Serial.println("Gönderim başarısız!");
  }
  delay(1000);
}