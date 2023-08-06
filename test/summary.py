import os
import pandas as pd
import math

antilog = 2

# idを計算. logを計算
id = math.log2(antilog)

# response_timeとmovement_timeを計算
rt = 0.5
mt = 0.8

output_file = './test/data/summary.csv'

# もし、all.csvがなかったら作成する
if not os.path.exists(output_file):
    all_df = pd.DataFrame(columns=['id', 'response_time', 'movement_time'])
    all_df.to_csv(output_file, index=False)

# all.csvの末尾に追加
all_df = pd.read_csv(output_file)
all_df.loc[len(all_df)] = [id, rt, mt]
all_df.to_csv(output_file, index=False)
