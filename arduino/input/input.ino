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
    float left_volt, center_volt, right_volt;

    left_volt = getVoltage( LEFT_VOL_PIN );
    center_volt = getVoltage( CENTER_VOL_PIN );
    right_volt = getVoltage( RIGHT_VOL_PIN );

    // Serial.print( "left: " );
    Serial.print( left_volt );
    Serial.print(",");
    // Serial.print( " center: " );
    Serial.print( center_volt );
    Serial.print(",");
    // Serial.print( " right: " );
    Serial.println( right_volt );
}
