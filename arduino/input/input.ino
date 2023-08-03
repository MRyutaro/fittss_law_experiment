#define LEFT_VOL_PIN A0
#define CENTER_VOL_PIN A1
#define RIGHT_VOL_PIN A2

void setup(){
    Serial.begin( 9600 );
}


float getVoltage( int pin ){
    int value;
    float volt;

    value = analogRead( pin );

    volt = value * 5.0 / 1023.0;

    return volt;
}

void loop(){
    float leftVolt, centerVolt, rightVolt;

    leftVolt = getVoltage( LEFT_VOL_PIN );
    centerVolt = getVoltage( CENTER_VOL_PIN );
    rightVolt = getVoltage( RIGHT_VOL_PIN );

    Serial.print( "left: " );
    Serial.print( leftVolt );
    Serial.print( " center: " );
    Serial.print( centerVolt );
    Serial.print( " right: " );
    Serial.println( rightVolt );
}
