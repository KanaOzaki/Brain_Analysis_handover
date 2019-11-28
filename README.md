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

### 0. ログアウト / 端末を閉じる　をしても実行を続ける方法
    nohup いつも通りのコマンド &
 これにより、標準出力は全てnohup.outというファイルに書き込まれる
 また、特定のファイルの出力を書き込みたい場合は、
    nohup いつも通りのコマンド > 書き込みたいファイル名 &
### 1.データの前処理　/src/preprocess/　(実行過程1)~3)に関しては改めて行う必要なし)
#### 1)VB_SNに関してテスト作成
    python make_SN.py
    
#### 2)意味表象行列の作成
例えば、タスクVBの訓練用を作成する場合

    python make_srm300.py VB train
    
#### 3)脳活動データの標準化
タスクVB、被験者SNの場合
    
    python Standardization_VB.py SN
    
タスクTV、被験者ANの場合

    python Standardization_TV.py AN
    
#### 4)脳活動データの次元削減 (閾値はコードの中で指定)
    python Brain_dimension_reduction_VB.py
    python Brain_dimension_reduction_TV.py
    
### 2.辞書学習 /src/model/
タスクVB、被験者SN、ボクセル抽出の閾値0.55、基底数900、時間差4秒、全サンプルを使用の場合
  
    python DL.py VB SN 0.55 900 4 1
    
### 3. スパースコーディング /src/model/
タスクVB、被験者SN、ボクセル抽出の閾値0.55、基底数900、時間差4秒、全サンプルを使用の場合

    python SP.py VB SN 0.55 900 4 1
    
### 4. 評価 /src/eval/
タスクVB、被験者SN、ボクセル抽出の閾値0.55、基底数900、時間差4秒、全サンプルを使用の場合

    python eval.py VB SN 0.55 900 4 1
