//https://github.com/sui77/rc-switch
//    off     on
//ch1 1208772 1208780 
//ch2 1208770 1208778 
//ch3 1208769 1208777 
//ch4 1208773 1208781
//ch5 1208771 1208779 

//ch6 1208774 1208782
//ch7 1208768 1208776

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
      mySwitch.send(1208772, 24); //ch1 off
    }
    if (incoming_char == '1') {
      mySwitch.send(1208780, 24); //ch1 on
    }
    if (incoming_char == '2') {
      mySwitch.send(1208770, 24); //ch2 off
    }
    if (incoming_char == '3') {
      mySwitch.send(1208778, 24); //ch2 on
    }
    if (incoming_char == '4') {
      mySwitch.send(1208769, 24); //ch3 off
    }
    if (incoming_char == '5') {
      mySwitch.send(1208777, 24); //ch3 on
    }
    if (incoming_char == '6') {
      mySwitch.send(1208773, 24); //ch4 off
    }
    if (incoming_char == '7') {
      mySwitch.send(1208781, 24); //ch4 on
    }
    if (incoming_char == '8') {
      mySwitch.send(1208771, 24); //ch5 off
    }
    if (incoming_char == '9') {
      mySwitch.send(1208779, 24); //ch5 on
    }
    if (incoming_char == 'a') {
      mySwitch.send(1208774, 24); //ch6 off
    }
    if (incoming_char == 'b') {
      mySwitch.send(1208782, 24); //ch6 on
    }
    if (incoming_char == 'c') {
      mySwitch.send(1208768, 24); //ch7 off
    }
    if (incoming_char == 'd') {
      mySwitch.send(1208776, 24); //ch7 on
    }
  }
}
