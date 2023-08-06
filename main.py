import serial
import time
import pandas as pd
from datetime import datetime
import random
import os


# arduinoからのデータを受け取る関数
def get_data_from_arduino(ser):
    """
    arduinoからのデータを受け取る関数

    Parameters
    ----------
    ser : serial.Serial
        シリアル通信の設定

    Returns
    -------
    data_from_arduino : list
        arduinoから受け取ったデータ. ['left_led', 'right_led', 'center_pin_volt', 'left_pin_volt', 'right_pin_volt']
    """
    try:
        line = ser.readline()
        stripped_str = str(line, 'ascii').strip()
        data_from_arduino = [float(d) for d in stripped_str.split(',')]
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{now}: {data_from_arduino}')

        return data_from_arduino

    except ValueError:
        print('ValueError')
        return None


def insert_line(data_from_arduino, df):
    """
    データリストの先頭に現在の時間を追加して、DataFrameに新しい行を追加する関数

    Parameters
    ----------
    data_from_arduino : list
        arduinoから受け取ったデータ
    df : DataFrame
        全てのデータを保存するDataFrame
    """
    # data_from_arduinoのコピーを作成
    insert_data = data_from_arduino.copy()

    # 現在の時間を取得
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # データリストの先頭に現在の時間を追加
    insert_data.insert(0, current_time)

    # DataFrameに新しい行を追加
    df.loc[len(df)] = insert_data

    return df


# 全てのLEDを消す
def all_led_off(ser):
    ser.write('left_led_off\n'.encode())
    ser.write('right_led_off\n'.encode())


if __name__ == '__main__':
    #####
    # ここを変える
    w = 0.5
    d = 0.5
    #####
    antilog = 2 * d / w

    ser = serial.Serial("COM3", 9600)
    time.sleep(2)

    # 真ん中の位置で安定させる
    count = 0
    while True:
        try:
            data_from_arduino = get_data_from_arduino(ser)
            if data_from_arduino is None:
                continue

            if len(data_from_arduino) != 5:
                continue

            # もしcenter_pin_voltが0.15V以下になるのが連続で10回あったらwhile文を抜ける
            if data_from_arduino[2] < 1.25:
                count += 1
                if count == 10:
                    break

        except ValueError:
            print('ValueError')
            continue

    print("実験を開始します")

    # 空のDataFrameを作成
    columns = ['time', 'left_led', 'right_led', 'center_pin_volt', 'left_pin_volt', 'right_pin_volt']
    saved_df = pd.DataFrame(columns=columns)

    # ランダムな時間待つ
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)

    # LEDを光らせる
    # ser.write('right_led_on\n'.encode())もしくはser.write('left_led_on\n'.encode())をランダムに選択
    led = random.choice(['right_led_on\n', 'left_led_on\n'])
    ser.write(led.encode())
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
            if data_from_arduino[3] < 1.25:
                if led == 'left_led_on\n':
                    print("実験が正常に終了しました")
                    break
                else:
                    print("実験が異常終了しました。LEDは左側、選択したのは右側です")
                    all_led_off(ser)
                    exit()
            elif data_from_arduino[4] < 1.25:
                if led == 'right_led_on\n':
                    print("実験が正常に終了しました")
                    break
                else:
                    print("実験が異常終了しました。LEDは右側、選択したのは左側です")
                    all_led_off(ser)
                    exit()

        except ValueError:
            print('ValueError')
            continue

    # フォルダを作成
    if not os.path.exists(f'./data/{antilog}'):
        os.makedirs(f'./data/{antilog}')

    # 現在の時間を取得
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

    # データをCSVファイルに保存
    saved_df.to_csv(f'./data/{antilog}/{current_time}.csv', index=False)

    # LEDを消す
    all_led_off(ser)
