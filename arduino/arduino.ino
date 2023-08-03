// 定義
#define RIGHT_LED_PIN 12
#define LEFT_LED_PIN 13

void setup() {
  Serial.begin(9600); // シリアル通信の初期化
  pinMode(RIGHT_LED_PIN, OUTPUT);
  pinMode(LEFT_LED_PIN, OUTPUT);
  digitalWrite(RIGHT_LED_PIN, LOW);
  digitalWrite(LEFT_LED_PIN, LOW);
}

void loop() {
  int data = Serial.read();

  // 右のLEDを制御するコマンド
  if (data = "right_led_on") {
    Serial.println("00");
    digitalWrite(RIGHT_LED_PIN, HIGH); // 右のLEDをオンにする
  }
  if (data = "right_led_off") {
    Serial.println("01");
    digitalWrite(RIGHT_LED_PIN, LOW); // 右のLEDをオフにする
  }

  // 左のLEDを制御するコマンド
  if (data = "left_led_on") {
    digitalWrite(LEFT_LED_PIN, HIGH); // 左のLEDをオンにする
  }
  if (data = "left_led_off") {
    digitalWrite(LEFT_LED_PIN, LOW); // 左のLEDをオフにする
  }
}
