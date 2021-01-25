import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


df = pd.read_csv("ratio.csv") #csv 파일 읽어오기

# 유클리디안 거리 계산
def l1_normalize(v):
    norm = np.sum(v)
    return v / norm

def ratio(happy, sad):
    input_ratio = [[happy, sad]] # 뇌파 측정 후 분류된 감정 비율
    df_norm_l1 = l1_normalize(df[["happy", "sad"]])
    dist_cal = euclidean_distances(input_ratio, df_norm_l1[:])
    df['dist'] = pd.DataFrame(dist_cal.reshape(9, 1))

    df_sorted = df.sort_values(by='dist', ascending=True)  # 거리 가까운 순으로 정렬

    input_img = 'pic0%d.jpg'%(df_sorted.iloc[0, 0])

    return input_img