#define RIGHT_LED 12
#define LEFT_LED 13
#define LEFT_VOL_PIN A0
#define CENTER_VOL_PIN A1
#define RIGHT_VOL_PIN A2

int is_Right_LED_On = 0;
int is_Left_LED_On = 0;
float left_volt, center_volt, right_volt;

void setup()
{
    Serial.begin(9600);
    Serial.setTimeout(10);
    pinMode(RIGHT_LED, OUTPUT);
    pinMode(LEFT_LED, OUTPUT);
}

float getVoltage( int pin ){
    int value;
    float volt;

    value = analogRead( pin );

    volt = value * 5.0 / 1023.0;

    return volt;
}

void loop()
{   
    // メッセージの受信
    String message = Serial.readStringUntil('\n');
    message.trim();

    // LEDの制御
    if (message == "right_led_on")
    {
        digitalWrite(RIGHT_LED, HIGH);
        is_Right_LED_On = 1;
    }
    else if (message == "right_led_off")
    {
        digitalWrite(RIGHT_LED, LOW);
        is_Right_LED_On = 0;
    }
    else if (message == "left_led_on")
    {
        digitalWrite(LEFT_LED, HIGH);
        is_Left_LED_On = 1;
    }
    else if (message == "left_led_off")
    {
        digitalWrite(LEFT_LED, LOW);
        is_Left_LED_On = 0;
    };

    // 電圧の取得
    left_volt = getVoltage( LEFT_VOL_PIN );
    center_volt = getVoltage( CENTER_VOL_PIN );
    right_volt = getVoltage( RIGHT_VOL_PIN );

    // メッセージの送信
    Serial.print(is_Left_LED_On);
    Serial.print(",");
    Serial.print(is_Right_LED_On);
    Serial.print(",");
    Serial.print(center_volt);
    Serial.print(",");
    Serial.print(left_volt);
    Serial.print(",");
    Serial.println(right_volt);
}
