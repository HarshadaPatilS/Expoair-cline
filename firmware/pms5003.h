#ifndef PMS5003_H
#define PMS5003_H

struct PMS5003Data {
  uint16_t pm1_0;
  uint16_t pm2_5;
  uint16_t pm10;
};

// Function to read PM data from the PMS5003 sensor
bool readPMS5003(HardwareSerial &s, PMS5003Data &out);

#endif // PMS5003_H