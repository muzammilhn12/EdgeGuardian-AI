#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;
const int VIBRATION_PIN = 4;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);
  pinMode(VIBRATION_PIN, INPUT);

  if (!mpu.begin()) {
    while (1) { delay(10); }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  int vibration_state = digitalRead(VIBRATION_PIN);

  float accel_x = a.acceleration.x / 9.80665;
  float accel_y = a.acceleration.y / 9.80665;
  float accel_z = a.acceleration.z / 9.80665;
  float magnitude = sqrt(accel_x * accel_x + accel_y * accel_y + accel_z * accel_z);

  Serial.print("{\"magnitude\":");
  Serial.print(magnitude, 3);
  Serial.print(",\"vibration\":");
  Serial.print(vibration_state);
  Serial.println("}");

  delay(10);
}
