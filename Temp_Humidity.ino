#include <LiquidCrystal.h>
int sensorValue;
int sensorValue1;
int sensorValue2;
void setup(){  
Serial.begin(9600);                            // sets the serial port to 9600
 }
void loop(){
sensorValue = analogRead(0);       // read analog input pin 0
Serial.print("MQ-8=");
Serial.print(sensorValue, DEC);               // prints the value read
Serial.println(" PPM");
delay(1000);      // wait 100ms for next reading
sensorValue1 = analogRead(1);       // read analog input pin 0
Serial.print("MQ-135=");
Serial.print(sensorValue1, DEC);               // prints the value read
Serial.println(" PPM");
delay(1000);      // wait 100ms for next reading
sensorValue2 = analogRead(2);       // read analog input pin 0
Serial.print("MQ-7=");
Serial.print(sensorValue1, DEC);               // prints the value read
Serial.println(" PPM");
delay(1000);      // wait 100ms for next reading

}
