import serial
import time


def main():
    #  COMポートを開く
    print("Open Port")
    ser = serial.Serial("COM3", 9600)
    time.sleep(2)

    while True:
        ser.write('ON\n'.encode())
        time.sleep(1.0)
        ser.write('OFF\n'.encode())
        time.sleep(1.0)


if __name__ == '__main__':
    main()
