#ifndef FIREBASE_UPLOAD_H
#define FIREBASE_UPLOAD_H

#include <Arduino.h>
#include "HTTPClient.h"
#include "ArduinoJson.h"

// Include the config file where Firebase URL is stored
extern "C" {
    #include "user_config.h"
}

void sendToFirebase(float pm25, float pm10, float lat, float lon, 
const char* deviceId);

#endif // FIREBASE_UPLOAD_H