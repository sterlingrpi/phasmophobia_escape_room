//https://github.com/sui77/rc-switch
//    on      off
//ch1 1208780 1208772
//ch2 1208778 1208770
//ch3 1208777 1208769
//ch4 1208781 1208773
//ch5 1208779 1208771

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();
char incoming_char = 0; 

void setup() {
  mySwitch.enableTransmit(10);  // Using Pin #10
  mySwitch.setPulseLength(197); // measured using receive
  mySwitch.send(1208770, 24); //off
//  mySwitch.send(1208778, 24); //on
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incoming_char = Serial.read();
    
    if (incoming_char == 48) {
      mySwitch.send(1208770, 24); //off
    }

    if (incoming_char == 49) {
      mySwitch.send(1208778, 24); //on
    }
  }
}
