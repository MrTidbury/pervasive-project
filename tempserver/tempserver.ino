#include <SPI.h> 
#include <Ethernet.h>
#include <EthernetUdp.h>

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xEF, 0xFE,0xED};
IPAddress ip(192,168,1,22); 
//IPAddress ip(192.168.0.11);//PUT THE IP ADDRESS HERE MAN
unsigned int localPort = 8888;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; 
int valueOfSens1 = 0;
int valueOfSens2 = 0;
int valueOfSens3 = 0;
int valueOfSens4 = 0;
int valueOfSens5 = 0;
int valueOfSens6 = 0;
int tempOfSens1 = 0;
int tempOfSens2 = 0;
int tempOfSens3 = 0;
int tempOfSens4 = 0;
int tempOfSens5 = 0;
int tempOfSens6 = 0;
int maxAllowedTemp = 85;

EthernetUDP Udp;

void setup()
{
  Ethernet.begin(mac,ip);
  Udp.begin(localPort);
  Serial.begin(9600);
  //NEED TO INIT THE SENSORS HERE STILL
}


void loop()
{
  valueOfSens1 = analogRead(A0);
  valueOfSens2 = analogRead(A1);
  valueOfSens3 = analogRead(A2);
  valueOfSens4 = analogRead(A3);
  valueOfSens5 = analogRead(A4);
  valueOfSens6 = analogRead(A5);
  tempOfSens1 = map(valueOfSens1,0,1023,0,110);
  tempOfSens2 = map(valueOfSens2,0,1023,0,110);
  tempOfSens3 = map(valueOfSens3,0,1023,0,110);
  tempOfSens4 = map(valueOfSens4,0,1023,0,110);
  tempOfSens5 = map(valueOfSens5,0,1023,0,110);
  tempOfSens6 = map(valueOfSens6,0,1023,0,110);
    if (maxAllowedTemp < tempOfSens1 || maxAllowedTemp < tempOfSens2 || maxAllowedTemp < tempOfSens3 || maxAllowedTemp < tempOfSens4 || maxAllowedTemp < tempOfSens5 || maxAllowedTemp < tempOfSens6)
  {
    Serial.println("startCooling");
  }
  else 
  {
    Serial.println("stopCooling");
  }
  int packageSize = Udp.parsePacket();
  if (packageSize)
  {
    Serial.write("udp package recived");
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.print( tempOfSens1);
    Udp.print(",");
    Udp.print( tempOfSens2);
    Udp.print(",");
    Udp.print( tempOfSens3);
    Udp.print(",");
    Udp.print( tempOfSens4);
    Udp.print(",");
    Udp.print( tempOfSens5);
    Udp.print(",");
    Udp.print( tempOfSens6);
    Udp.endPacket(); 
  }
  delay(250);
}

