#!=usr/bin/python
#-*- coding: utf-8 -*-
#意味表象ベクトルと最も近い単語（品詞ごとも可）上位5個出力してファイルに保存
from gensim import corpora, matutils
import gensim
import h5py
import numpy as np
import scipy.stats as sp

# word2vecファイル
w2v_filename = '../../data/entity_vector/nwjc_word_skip_300_8_25_0_1e4_6_1_0_15.txt.vec'
W2V_model = gensim.models.KeyedVectors.load_word2vec_format(w2v_filename)

# 辞書学習で作られた辞書の読み込み
dict_srm = np.load("../../data/Dict/VB/Dict_SN_pred0.55_base900_sec4_sample1.pickle")

# 辞書の中から意味表象辞書のみを取り出す
dict_srm = np.array(dict_srm)
dict_srm = dict_srm.T 

dict_srm = dict_srm[-300:]
dict_srm = dict_srm.T 
print(dict_srm.shape)

# 語彙ファイル
vocab_file=open('../../original_data/TV/jawiki160111S1000W10SG_vocab.txt','r')

# 語彙リスト作成
vocab_list = {}
for line in vocab_file:
    line = line.strip()
    word_list = line.split(' ')
    word_list = word_list[0].split('.')
    vocab_list[word_list[0]] = word_list[1]

# 語彙リストに含まれている名詞、形容詞、動詞のみについてcos類似度上位5つの単語を出力
for i,vector in enumerate(dict_srm):
    counter = 0 #上位5単語まで表示するためのカウンター
    words = W2V_model.most_similar([vector], [], 5000)
    print("基底 " + str(i) + "-------")
    for word in words:
        if(word[0] in vocab_list.keys()):
            word_type = vocab_list[word[0]]
            if(word_type == "n" or word_type == "a" or word_type == "v"):
                counter += 1
                print (word_type + " " + word[0] + ":" + str(word[1]))
        if counter >= 5:
            break
    print("-------------------------------")
