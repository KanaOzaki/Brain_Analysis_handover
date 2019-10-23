#!=usr/bin/python
#-*- coding: utf-8 -*-
#Normalization.py

import sys
import numpy as np
from scipy.io import loadmat
import pickle

DATA_DIR = '../original_data'

def Standardization(X, mean, sd):

	return (float(X - mean)/sd)

def main():

	args = sys.argv
	sub = args[1]

	##1. 訓練データを標準化
	#大脳皮質のみのpickleデータを読み込み
	with open(DATA_DIR + '/TV/preprocess/' + sub + '_Fix_brain_train_preprocess.pickle', 'rb') as f:
		train_data = pickle.load(f, encoding='latin1')

	# 平均0、分散1に正規化
	mean = np.mean(train_data)
	sd = np.std(train_data)
	train_data = np.array([[Standardization(X, mean, sd) for X in row] for row in train_data])

	print(np.mean(train_data))
	print(np.std(train_data))
	print(train_data.shape)

	# 標準化済みtrain_data保存
	with open(DATA_DIR + '/TV/' + sub + '_Fix_brain_train_std.pickle', 'wb') as f:
			pickle.dump(train_data, f)

	##2. テストデータを標準化
	test_data = loadmat(DATA_DIR + '/TV/ROW/NishidaFixVimeo_' + sub + '.Val01.mat')
	test_data = test_data['resp']

	#マスキングデータで大脳皮質のみ取り出す
	vset = loadmat(DATA_DIR + '/TV/vset/' +  sub + '.vset/vset_099.mat')
	vset = vset['tvoxels']
	vset = [ flatten for inner in vset for flatten in inner ]
	test_data = test_data[:, vset]

	# 平均0、分散1に正規化
	mean = np.mean(test_data)
	sd = np.std(test_data)
	test_data = np.array([[Standardization(X, mean, sd) for X in row] for row in test_data])

	print(np.mean(test_data))
	print(np.std(test_data))
	print(test_data.shape)

	# 標準化したtest_data保存
	with open(DATA_DIR + '/TV/' + sub + '_Fix_brain_test_std.pickle', 'wb') as f:
		pickle.dump(test_data, f)


if __name__ == '__main__':
	main()
