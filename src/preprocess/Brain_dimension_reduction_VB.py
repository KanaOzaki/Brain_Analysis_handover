#!=usr/bin/python
#-*- coding: utf-8 -*-
#Brain_dimention_reduction_VB.py

##このプログラムは、VBにおける脳活動データの次元を削減する.
##予測精度の閾値を設定し、その閾値以上のボクセルのみを抽出し、
##使用する脳活動行列として保存する.
##trainとtest同時に行う.

from scipy.io import loadmat
import pickle
import numpy as np

DATA_DIR = '../original_data'
subjects = ['ST', 'SN', 'DK']
threshold = 0.55


def reduce_dimention(brain_data, ac_data, threshold):

	# ROIの相関が高い領域だけを抽出.(ある一定の値以上のものを調べる)
	Brain_reduced = []
	for i, cor in enumerate(ac_data):
		if cor > threshold:
			Brain_reduced.append(brain_data[:,i])
	Brain_reduced = np.array(Brain_reduced)
	Brain_reduced = Brain_reduced.T

	return Brain_reduced

def main():

	for sub in subjects:

		print(sub)

		# 精度データ読み込み
		ac_data = loadmat(DATA_DIR + '/VB/VB_PredAcc/VB_' + sub + '.mat')
		ac_data = ac_data['ccs']
		print(len(ac_data))

		# 脳活動データ読み込み(train, test)
		# DKのみデータが大きいので、2つに分けて保存
		if sub == 'DK':
			with open(DATA_DIR + '/VB/' + sub + '_VB_brain_train_std1.pickle', 'rb') as f:
				train_data1 = pickle.load(f, encoding='latin1')
			with open(DATA_DIR + '/VB/' + sub + '_VB_brain_train_std2.pickle', 'rb') as f:
				train_data2 = pickle.load(f, encoding='latin1')
			train_data = np.r_[train_data1, train_data2]
		else:
			with open(DATA_DIR + '/VB/' + sub + '_VB_brain_train_std.pickle', 'rb') as f:
				train_data = pickle.load(f, encoding='latin1')

		with open(DATA_DIR +  '/VB/' + sub + '_VB_brain_test_std.pickle', 'rb') as f:
			test_data = pickle.load(f, encoding = 'latin1')

		print('削減前')
		print(train_data.shape)
		print(test_data.shape)

		# 次元削減
		train_reduced = reduce_dimention(train_data, ac_data, threshold)
		test_reduced = reduce_dimention(test_data, ac_data, threshold)

		print('削減後')
		print (train_reduced.shape)
		print (test_reduced.shape)

		# 保存
		with open('../../data/Brain/VB/' + sub + '_train_reduced_'+ str(threshold) + '.pickle', 'wb') as f:
			pickle.dump(train_reduced, f)

		with open('../../data/Brain/VB/' + sub + '_test_reduced_'+ str(threshold) + '.pickle', 'wb') as f:
			pickle.dump(test_reduced, f)

if __name__ == '__main__':
	main()
