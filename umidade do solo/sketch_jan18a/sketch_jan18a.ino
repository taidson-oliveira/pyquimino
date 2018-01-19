#include <Thermistor.h>

Thermistor temp(0);

int pin_umd = A1;
int pin_temp = A0;

int button = 8;
int button_state =0;

void setup(){
  Serial.begin(9600);
  pinMode(pin_umd,INPUT);
  pinMode(pin_temp,INPUT);
  pinMode(button,INPUT_PULLUP);
}
void loop(){

  button_state = digitalRead(button);
  //int umd = analogRead(pin_umd);
  int temperatura = temp.getTemp();
  
  if (button_state == HIGH) {
     Serial.println(-100);
     
  }
  else{
    Serial.println(temperatura,DEC);
  }
  delay(1000);
}

