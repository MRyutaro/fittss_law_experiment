import serial
import time


def right_led_on(ser):
    str = "right_led_on"
    ser.write(str.encode("utf-8"))
    print("right_led_on")
    time.sleep(1)


def right_led_off(ser):
    str = "right_led_off"
    ser.write(str.encode("utf-8"))
    print("right_led_off")
    time.sleep(1)


def left_led_on(ser):
    str = "left_led_on"
    ser.write(str.encode("utf-8"))
    print("left_led_on")
    time.sleep(1)


def left_led_off(ser):
    str = "left_led_off"
    ser.write(str.encode("utf-8"))
    print("left_led_off")
    time.sleep(1)


def main():
    #  COMポートを開く
    print("Open Port")
    ser = serial.Serial("COM3", 9600)
    print(ser)
    while True:
        try:
            right_led_on(ser)
            right_led_off(ser)
            left_led_on(ser)
            left_led_off(ser)

            line = ser.readline()
            line_disp = line.strip().decode('UTF-8')
            print(line_disp)

        except KeyboardInterrupt:
            print("Close Port")
            ser.close()

        except Exception as e:
            print(e)
            print("Close Port")
            ser.close()


if __name__ == '__main__':
    main()
