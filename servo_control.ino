// prova servo
#include <Servo.h>
  
// ogni 2,5 secondi lo faccio ruotare 


Servo Servo1;
int servoPin = 9;
int trigPin = 10;
int echoPin = 11;
int goal = 0;
int sum = 3;
bool firstTime = true; 
int duration;
int cm;

void setup() {
  // put your setup code here, to run once:ù
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Servo1.attach(servoPin);
  Servo1.write(goal);
}

void loop(){

  // sono passati 2,5 secondi --> 150°
  /*
  int reading = analogRead(potPin);
  int angle = map(reading, 0, 1023, 0, 180);
  Servo1.write(angle);
  */

  if (((goal == 180) || (goal == 0)) && (firstTime != true)) {
    sum = sum * -1;
  }

  goal = goal + sum;
  Servo1.write(goal);
  firstTime = false;

  // get the distance
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  cm = microsecondsToCentimeters(duration);

  Serial.print(cm);
  Serial.print("/");
  Serial.println(goal);  // valore temporaeo. Da cambiare quando posso calcolare la distanza
  delay(13);

}




long microsecondsToCentimeters(long microseconds) {
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the object we
  // take half of the distance travelled.
  return microseconds / 29 / 2;
}

