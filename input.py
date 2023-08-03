import serial
import time
import pandas as pd
from datetime import datetime

ser = serial.Serial("COM3", 9600)
time.sleep(2)

# 空のDataFrameを作成
columns = ['time', 'left_pin_volt', 'center_pin_volt', 'right_pin_volt']
data_df = pd.DataFrame(columns=columns)

while True:
    line = ser.readline()
    stripped_str = str(line, 'ascii').strip()
    try:
        data = [float(d) for d in stripped_str.split(',')]

        # 現在の時間を取得
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # データリストの先頭に現在の時間を追加
        data.insert(0, current_time)

        # DataFrameに新しい行を追加
        data_df.loc[len(data_df)] = data

        print(data)

        # 何らかの条件で処理を終了する場合はbreak文を追加
        if len(data_df) > 100:
            break

    except ValueError:
        print('ValueError')
        continue


# 現在の時間を取得
current_time = datetime.now().strftime('%Y%m%d%H%M%S')

# データをCSVファイルに保存
data_df.to_csv(f'./data/{current_time}.csv', index=False)
