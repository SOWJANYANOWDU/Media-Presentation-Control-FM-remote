
//to map the address of remote to keys on keyboard
#include <IRremote.hpp>

#define IR_RECEIVE_PIN 2  // VS1838B OUT connected to D2

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
}

void loop() {
  if (IrReceiver.decode()) {
    unsigned long code = IrReceiver.decodedIRData.decodedRawData;
    Serial.println(code, HEX);  // Send button code to PC
    IrReceiver.resume();
  }
}



// //to check the address of pins on the fm remote
// #include <IRremote.hpp>  // New library include
// #define IR_RECEIVE_PIN 11   // Pin where IR receiver is connected

// void setup() {
//   Serial.begin(9600);
//   IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Start receiver
//   Serial.println("IR Receiver is ready...");
// }

// void loop() {
//   if (IrReceiver.decode()) {
//     // Print raw data (HEX code of pressed button)
//     Serial.print("IR code: 0x");
//     Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
//     IrReceiver.resume();  // Receive next value
//   }
// }








