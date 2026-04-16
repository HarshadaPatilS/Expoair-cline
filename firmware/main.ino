#include <Arduino.h>
#include "WiFi.h"
#include <FirebaseESP32.h>

// Include the config file where WiFi credentials are stored
extern "C" {
    #include "user_config.h"
}

// Initialize Firebase and other components
void setup() {
  Serial.begin(115200); // Start serial communication

  // Connect to WiFi using
credentials from config.h
  WiFi.begin(WIFI_SSID,
WIFI_PASSWORD);
  while (WiFi.status() !=
WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");

  // Initialize Firebase with your database URL and auth token
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH_TOKEN);

  // Setup the PMS5003 sensor on serial2
  Serial2.begin(9600); // Set baud rate for PMS5003

  Serial.println("Setup complete");
}

// Placeholder function to simulate sending data to Firebase
void sendToFirebase(float pm25, float pm10, double lat, double lon) {
  // This function is a placeholder. In a real application, you would       
use the FirebaseESP32 library to send data.
  Serial.print("Sending data to Firebase: ");
  Serial.println("PM2.5: " + String(pm25) + ", PM10: " + 
String(pm10));
}
  delay(100);

  Serial2.write(0x42); // Start byte
  Serial2.write(0x4D); // Product ID
  Serial2.write(0x00); // Length of payload (low byte)
  Serial2.write(0x08); // Length of payload (high byte)

  delayMicroseconds(100);

  uint8_t buffer[32];
  int bytesRead = Serial2.readBytes(buffer, sizeof(buffer));

  if (bytesRead == sizeof(buffer)) {
    float pm2_5 = ((buffer[6] << 8) | buffer[7]) / 10.0;
    float pm10 = ((buffer[4] <<
8) | buffer[5]) / 10.0;

    Serial.print("PM2.5: ");
    Serial.print(pm2_5);
    Serial.print(", PM10: ");
    Serial.println(pm10);

    // Placeholder for sending data to Firebase
    sendToFirebase(pm2_5, pm10, 37.7749, -122.4194); // Example
coordinates (San Francisco)
  }
}

// Main loop function
void loop() {
  readPMS5003();

  // You can add delay here if you want to control the frequency of
readings or uploads
  delay(60 * 1000); // Read every minute
}