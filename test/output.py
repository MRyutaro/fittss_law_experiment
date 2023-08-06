import serial
import time


def main():
    #  COMポートを開く
    print("Open Port")
    ser = serial.Serial("COM3", 9600)
    time.sleep(2)

    while True:
        ser.write('right_led_on\n'.encode())
        time.sleep(1)
        ser.write('right_led_off\n'.encode())
        time.sleep(1)
        ser.write('left_led_on\n'.encode())
        time.sleep(1)
        ser.write('left_led_off\n'.encode())
        time.sleep(1)


if __name__ == '__main__':
    main()
