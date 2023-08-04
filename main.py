import serial
import time
import pandas as pd
from datetime import datetime
import random
import os


# arduinoからのデータを受け取る関数
def get_data_from_arduino(ser):
    try:
        line = ser.readline()
        stripped_str = str(line, 'ascii').strip()
        data_from_arduino = [float(d) for d in stripped_str.split(',')]

        return data_from_arduino

    except ValueError:
        print('ValueError')
        return None


def insert_line(data_from_arduino, df):
    # 現在の時間を取得
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # データリストの先頭に現在の時間を追加
    data_from_arduino.insert(0, current_time)

    # DataFrameに新しい行を追加
    df.loc[len(df)] = data_from_arduino

    return df


if __name__ == '__main__':
    #####
    # ここを変える
    w = 0.5
    d = 0.5
    #####
    antilog = 2 * d / w

    ser = serial.Serial("COM3", 9600)
    time.sleep(2)

    # 空のDataFrameを作成
    columns = ['time', 'left_led', 'right_led', 'center_pin_volt', 'left_pin_volt', 'right_pin_volt']
    saved_df = pd.DataFrame(columns=columns)

    # 真ん中の位置で安定させる
    count = 0
    while True:
        try:
            data_from_arduino = get_data_from_arduino(ser)
            if data_from_arduino is None:
                continue

            saved_df = insert_line(data_from_arduino, saved_df)

            # もしcenter_pin_voltが0.15V以下になるのが連続で10回あったらwhile文を抜ける
            if data_from_arduino[3] < 0.15:
                count += 1
                if count == 10:
                    break

        except ValueError:
            print('ValueError')
            continue

    # ランダムな時間待つ
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)

    # LEDを光らせる
    # ser.write('right_led_on\n'.encode())もしくはser.write('left_led_on\n'.encode())をランダムに選択
    led = random.choice(['right_led_on', 'left_led_on'])
    ser.write(f'{led}\n'.encode())
    data_from_arduino = get_data_from_arduino(ser)
    saved_df = insert_line(data_from_arduino, saved_df)

    # 電圧を取得する
    while True:
        try:
            data_from_arduino = get_data_from_arduino(ser)
            if data_from_arduino is None:
                continue

            saved_df = insert_line(data_from_arduino, saved_df)

            # 左右どっちかの電圧が0.15V以下になり、かつ、それがLEDが光っている方と同じだったらwhile文を抜ける
            # そうじゃなかったらexit()でプログラムを終了する

        except ValueError:
            print('ValueError')
            continue

    # フォルダを作成
    if not os.path.exists(f'./data/{antilog}'):
        os.makedirs(f'./data/{antilog}')

    # 現在の時間を取得
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')

    # データをCSVファイルに保存
    saved_df.to_csv(f'./data/{antilog}/{current_time}.csv', index=False)
