#!=usr/bin/python
#-*- coding: utf-8 -*-
#スパース行列のサンプルごとの非ゼロ要素数と非ゼロ成分番号を出力
import numpy as np
import collections
import random


# データの保存場所パス
DATA_DIR = "../../data"
# 出力ファイル名指定
filepath = 'random_SN_sec4_sample1_2.txt'

#1.係数行列の読み込み
coef=np.load( DATA_DIR + "/Dict/VB/Coef_SN_pred0.55_base900_sec4_sample1.pickle")
coef=np.array(coef)
print (coef.shape[1])


#2.選択した基底が大きく寄与しているサンプルをとってくる
## sampling数分、サンプル数までの大きさからランダムにリストを作る
sampling = 100
base = range(coef.shape[1])
random_base = random.sample(base, sampling)
counter = 0

## ランダムに取り出したそれぞれの基底に対して、上位5サンプルを取ってくる
with open(filepath, mode = 'w') as result_file:
    for i in random_base:
        coef_base = coef[:,i]
        sample_set = []
        for num, value in enumerate(coef_base):
            sample_set.append([num,value])
            ## setをソート、上位5個を取ってくる
            sample_set=sorted(sample_set, key=lambda x:x[1])
            sample_set.reverse() #reverseなしだと回数少ない基底
        # もし0以下の係数が1つでも含まれていたら飛ばす
        if sample_set[4][1] <= 0.0:
            continue
        result_file.write(str(i))
        result_file.write('\n')
        for j in range(5):
            sample_num = sample_set[j][0]*2
            result_file.write("サンプル番号 : ")
            result_file.write(str(sample_num))
            result_file.write("  係数 : ")
            result_file.write(str(sample_set[j][1]))
            result_file.write('\n')
        counter += 1
        if counter >= 50:
            break
