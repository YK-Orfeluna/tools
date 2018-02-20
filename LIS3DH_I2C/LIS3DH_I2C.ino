#include <Wire.h>
const int SLAVE = 0x18;
const int OUT_X_L = 0x28;
const int OUT_X_H = 0x29;
const int OUT_Y_L = 0x2A;
const int OUT_Y_H = 0x2B;
const int OUT_Z_L = 0x2C;
const int OUT_Z_H = 0x2D;
const char TAB = "\t";

byte resisterRead(byte reg, int b = 1) {
  Wire.beginTransmission(SLAVE);
  Wire.write(reg);
  if (Wire.endTransmission() == 0) {
    Wire.requestFrom(SLAVE, b);
    if (Wire.available() > 0) {
      return Wire.read();
    }else{
      return 0;
    }
  }
}

int x_accel(){
  return makeWord(resisterRead(OUT_X_H), resisterRead(OUT_X_L));
}

int y_accel(){
  return makeWord(resisterRead(OUT_Y_H), resisterRead(OUT_Y_L));
}

int z_accel(){
  return makeWord(resisterRead(OUT_Z_H), resisterRead(OUT_Z_L));
}

void setup() {
  const int BPS = 9600;

  const int WHO_AM_I = 0x0F;
  const int CTRL_REG1 = 0x20;
  const int CONNECT = 0x33;
  const int START = 0x7F;

  const int LED = 13;
  
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);

  Wire.begin();
  Serial.begin(BPS);

  if (resisterRead(WHO_AM_I) == CONNECT) {
    Wire.beginTransmission(SLAVE);
    Wire.write(CTRL_REG1);
    Wire.write(START);
    Wire.endTransmission();
    
    digitalWrite(LED, HIGH);
    Serial.println("Connection is Succeeded");
  } else {
    Serial.println("Connection is Failed");
  }
}

void loop() {
  Serial.print(x_accel());
  Serial.print("\t");
  Serial.print(y_accel());
  Serial.print("\t");
  Serial.println(z_accel());
  delay(100);
}


