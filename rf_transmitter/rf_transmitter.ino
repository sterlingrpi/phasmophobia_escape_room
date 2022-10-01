//https://github.com/sui77/rc-switch
//    on      off
//ch1 1208780 1208772
//ch2 1208778 1208770
//ch3 1208777 1208769
//ch4 1208781 1208773
//ch5 1208779 1208771

//ch6 774524 774516
//ch7 774522 774514
//ch8 774521 774513
//ch9 774525 774517
//ch10 774523 774515

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();
char incoming_char; 

void setup() {
  mySwitch.enableTransmit(10);  // Using Pin #10
  mySwitch.setPulseLength(197); // measured using receive
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incoming_char = Serial.read();
    if (incoming_char == '0') {
      mySwitch.send(1208780, 24); //ch1 on
    }
    if (incoming_char == '1') {
      mySwitch.send(1208772, 24); //ch1 off
    }
    if (incoming_char == '2') {
      mySwitch.send(1208778, 24); //ch2 on
    }
    if (incoming_char == '3') {
      mySwitch.send(1208770, 24); //ch2 off
    }
    if (incoming_char == '4') {
      mySwitch.send(1208777, 24); //ch3 on
    }
    if (incoming_char == '5') {
      mySwitch.send(1208769, 24); //ch3 off
    }
    if (incoming_char == '6') {
      mySwitch.send(1208781, 24); //ch4 on
    }
    if (incoming_char == '7') {
      mySwitch.send(1208773, 24); //ch4 off
    }
    if (incoming_char == '8') {
      mySwitch.send(1208779, 24); //ch5 on
    }
    if (incoming_char == '9') {
      mySwitch.send(1208771, 24); //ch5 off
    }
    if (incoming_char == 'a') {
      mySwitch.send(774524, 24); //ch6 on
    }
    if (incoming_char == 'b') {
      mySwitch.send(774516, 24); //ch6 off
    }
    if (incoming_char == 'c') {
      mySwitch.send(774522, 24); //ch7 on
    }
    if (incoming_char == 'd') {
      mySwitch.send(774514, 24); //ch7 off
    }
    if (incoming_char == 'e') {
      mySwitch.send(774521, 24); //ch8 on
    }
    if (incoming_char == 'f') {
      mySwitch.send(774513, 24); //ch8 off
    }
    if (incoming_char == 'g') {
      mySwitch.send(774525, 24); //ch9 on
    }
    if (incoming_char == 'h') {
      mySwitch.send(774517, 24); //ch9 off
    }
    if (incoming_char == 'i') {
      mySwitch.send(774523, 24); //ch10 on
    }
    if (incoming_char == 'j') {
      mySwitch.send(774515, 24); //ch10 off
    }
  }
}