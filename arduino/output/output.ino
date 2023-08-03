#define RIGHT_LED 13
#define LEFT_LED 12

void setup()
{
  Serial.begin(9600);
  pinMode(RIGHT_LED, OUTPUT);
  pinMode(LEFT_LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  String message = Serial.readStringUntil('\n');
  message.trim();
  if (message == "right_led_on") {
    digitalWrite(RIGHT_LED, HIGH);
  } else if (message == "right_led_off") {
    digitalWrite(RIGHT_LED, LOW);
  };
  if (message == "left_led_on") {
    digitalWrite(LEFT_LED, HIGH);
  } else if (message == "left_led_off") {
    digitalWrite(LEFT_LED, LOW);
  };
}
