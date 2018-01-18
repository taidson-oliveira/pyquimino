int pin_umd = A1;

int umd = 0;

void setup(){
  Serial.begin(9600);
  pinMode(pin_umd,INPUT);
}
void loop(){
  umd = analogRead(pin_umd);
  Serial.print(umd);
  delay(1000);
}
