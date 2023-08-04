#define RIGHT_LED 13
#define LEFT_LED 12

void setup()
{
  Serial.begin(9600);
  pinMode(RIGHT_LED, OUTPUT);
  pinMode(LEFT_LED, OUTPUT);
  int is_Right_LED_On = 0;
  int is_Left_LED_On = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  String message = Serial.readStringUntil('\n');
  message.trim();
  if (message == "right_led_on") {
    digitalWrite(RIGHT_LED, HIGH);
    is_Right_LED_On = 1;
  } else if (message == "right_led_off") {
    digitalWrite(RIGHT_LED, LOW);
    is_Right_LED_On = 0;
  };
  if (message == "left_led_on") {
    digitalWrite(LEFT_LED, HIGH);
    is_Left_LED_On = 1;
  } else if (message == "left_led_off") {
    digitalWrite(LEFT_LED, LOW);
    is_Left_LED_On = 0;
  };

  Serial.print(is_Left_LED_On);
  Serial.print(",");
  Serial.println(is_Right_LED_On);
}
