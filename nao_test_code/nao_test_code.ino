

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  static bool ledOn = false;
  Serial.println("0, 1, 2, 3, 4, 5, 6, 7");
  if(ledOn){
    digitalWrite(13, LOW);
    ledOn = false;
  }
  else{
    digitalWrite(13, HIGH);
    ledOn = true;
  }
  delay(500);
}
