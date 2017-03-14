int led = 9;           // the PWM pin the LED is attached to
int brightness = 200;    // how bright the LED is

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
  pinMode(led, OUTPUT);
}

void loop() {
  int incoming = 0;
  String data = " ";
  
  if (Serial.available()) {
    data = Serial.readString();
    Serial.println(data);
  }
  
  if (data == "1"){
    analogWrite(led, brightness);
  }
  
  if (data == "0"){
    analogWrite(led, 0);
  }
  
  delay(500); // delay for 1/10 of a second
}
