int LED = 9; // the PWM pin the LED is attached to
float brightness = 0; // LED brightness
float locationBounds[] = {-25.0, 50.0}; // Record {low, high} temperatures for location

// PARAMETERS TO BE EDITED
float SanDiego[] = {-4.0, 44.0}; // Record {low, high} temperatures in San Diego

void setup() {
  
  Serial.begin(9600); // set the baud rate
//  Serial.println("Ready"); // print "Ready" once
  pinMode(LED, OUTPUT);
  
  getLocationBounds(SanDiego);
  Serial.println(locationBounds[0]);
  Serial.println(locationBounds[1]);
  
}

void loop() {
  
  String data = "";
  float value = 0.0;
  
  if (Serial.available()) {
    data = Serial.readString();
    value = data.toFloat();
    Serial.println(data);
  }

  brightness = map(value, locationBounds[0], locationBounds[1], 0.0, 255.0);
  analogWrite(LED, brightness);
  
  delay(500);
}

void getLocationBounds(float location[]) {
  locationBounds[0] = location[0];
  locationBounds[1] = location[1];
//  memcpy(locationBounds, location,2);
}

