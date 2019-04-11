

#include <SoftwareSerial.h>

#define RX  9// Connected to Digital Pin 8 of Arduino
#define TX 8// Connected to Digital Pin 9 of Arduino


String AP = "2015";       // Your Access Point Name
String PASS = "2k152k15";     // Your Password

/* 
 *  Here we are sending data to ThingSpeak API. 
 *  Create a free account in ThingSpeak.
 *  Then create a new channel. 
 *  Copy the API key for your new channel to below API String
 *  You can later browse the channel visualization to view the data
*/
String API = "K4PRH52FKDO1HY18";   // ThingSpeak API Key
String HOST = "api.thingspeak.com";
String PORT = "80";
const int buzzer =4;

int sensorValue;
int sensorValue1;
int sensorValue2;

SoftwareSerial esp8266(RX,TX); // Initializing esp8266 package with proper pins

void setup() {
  esp8266.begin(115200);
 
   Serial.begin(9600);// Setting the baud rate       
  esp8266.println("AT");    // Sending AT command
  delay(1500);              // Delays are added between each esp8266 serial print for giving time to complete the respective command.
  esp8266.println("AT+CWMODE=1");   // Command to choose the Mode: 1 - Station Mode(client), 2 - AP Mode (Host), 3 - Station+AP (Dual Mode)// set wifi mode
  delay(1500);
  esp8266.println("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"");  // Giving AP Name and Password for connection
  delay(1500);
pinMode(buzzer, OUTPUT); // Set buzzer - pin 4 as an output

}

void loop() {
  sensorValue = analogRead(0);       // read analog input pin 0

  sensorValue1 = analogRead(1);       // read analog input pin 1

  sensorValue2 = analogRead(2);       // read analog input pin 2
   if(sensorValue>300){
   tone(buzzer, 1000); // Send 1KHz sound signal...
  delay(1000);        // ...for 1 sec
  noTone(buzzer);     // Stop sound...
  delay(1000);        // ...for 1sec
  }
 
  String data = "GET /update?api_key="+ API +"&"+ "field1="+String(sensorValue)+"&field2="+String(sensorValue1)+"&field3="+String(sensorValue2); // Url to send data to ThingSpeak Channel
  esp8266.println("AT+CIPMUX=1");//Enable multiple connection. to make sure that the data sender and receiver will not be replaced by other devices. 
  delay(100);
  esp8266.println("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT);  // Establishing TCP connection with Host and Port (here ThingSpeak API on port 80)
  delay(100);
  esp8266.println("AT+CIPSEND=0," +String(data.length()+4));    // Setting up the length of the data.
  delay(100);
  esp8266.println(data);      // Sending Data to the Url
  delay(100);
  esp8266.println("AT+CIPCLOSE=0");   // Closing the TCP Connection
}
