#define RIGHT_LED 13
#define LEFT_LED 12

void setup()
{
  Serial.begin(9600);
  pinMode(RIGHT_LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  String message = Serial.readStringUntil('\n');
  message.trim();
  if (message == "ON") {
    digitalWrite(RIGHT_LED, HIGH);
  } else if (message == "OFF") {
    digitalWrite(RIGHT_LED, LOW);
  }
}
