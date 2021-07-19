
float readPin1=A1;
float V1=0.0000;

float readPin2=A2;
float V2=0.0000;

float readPin3=A3;
float V3=0.0000;

int delayTime=1000;
void setup() {
  pinMode(readPin1,INPUT);
  pinMode(readPin2,INPUT);
  pinMode(readPin3,INPUT);
  Serial.begin(19200);
}

void loop() {
 V1=analogRead(readPin1);
 V2=analogRead(readPin2);
 V3=analogRead(readPin3);
  Serial.print(V1);
  Serial.print("/");
  Serial.print(V2);
  Serial.print("/");
  Serial.println(V3);
 delay(delayTime); 
}
