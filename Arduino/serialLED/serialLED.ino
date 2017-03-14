int led = 9;           // the PWM pin the LED is attached to
int brightness = 200;    // how bright the LED is

void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once
pinMode(led, OUTPUT);
}

void loop() {
//char inByte = ' ';
//char data[] = "hello"; 
//char data;
String data = " ";
//if(Serial.available()){ // only send data back if data has been sent
//  char inByte = Serial.read(); // read the incoming data
//  Serial.println(inByte); // send the data back in a new line so that it is not all one long line
//}
if (Serial.available()) {
  data = Serial.readString();
  Serial.println(data);
}
if (data){
  analogWrite(led, brightness);
  delay(100);
  analogWrite(led, 0);
}
delay(500); // delay for 1/10 of a second
}
