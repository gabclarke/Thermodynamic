void setup() {
  size(200, 200);
}

void draw() { 
  // draw() must be present for mousePressed() to work
}

void mousePressed() {
  println("Opening");
  launch("/Python/darkskyTemp.py");
  println("success");
}