# Brain_Analysis 引き継ぎ

2018年から2019年にかけて行った「脳活動データ及び意味表象情報の対応関係の調査」の引き継ぎ用のコード

## 必要な環境
* python3.6
* scipy
* numpy
* pickle
* janome
* gensim
* sklearn

## 実行の流れ
### 1.データの前処理　実行例　(実行過程1)~3)に関しては改めて行う必要なし　./preprocess/)
#### 1)VB_SNに関してテスト作成
    python make_SN.py
#### 2)意味表象行列の作成
    python make_srm300.py VB train

    
