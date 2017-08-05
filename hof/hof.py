# coding: utf-8

import numpy as np

# 計算は全てdegreesではなくradiansで行う
RANGE = (0, np.pi*2)
TH = np.radians([0, 45, 90, 135, 180, 225, 270, 315, 360]).astype(np.float64)

# binsは現在8のみ対応

def hof_features(pre, now, bins=8, weights=True, normalize=True) :

	rad = np.arctan2(now, pre)								# オプティカルフローの角度を求める
	hist = np.histogram(rad, bins=bins, range=RANGE)[0]		# ヒストグラムの計算
	#print("histogram = \n", hist)

	if weights :
		
		dis =  np.abs(now - pre)							# 各オプティカルフローの距離の合計値を求める
		
		a = dis[rad<TH[1]].sum()							# binごとにオプティカルフローの合計値を求める

		b = dis[TH[1]<=rad]
		b = b[b<TH[2]].sum()

		c = dis[TH[2]<=rad]
		c = c[c<TH[3]].sum()

		d = dis[TH[3]<=rad]
		d = d[d<TH[4]].sum()

		e = dis[TH[4]<=rad]
		e = e[e<TH[5]].sum()

		f = dis[TH[5]<=rad]
		f = f[f<TH[6]].sum()

		g = dis[TH[6]<=rad]
		g = g[g<TH[7]].sum()

		h = dis[TH[7]<=rad].sum()

		
		w = np.array([a, b, c, d, e, f, g, h])				# 合計値をまとめて重みとする
		#print("weights = \n", w)

		# ヒストグラムに重み付けを行う
		hist = hist * w
	
	if normalize :
		hist = hist / hist.sum()							# 合計値が1になるように正規化する

	return hist


N = 1000

a1 = np.random.rand(N)*100
a2 = np.random.rand(N)*100

print(hof_features(a1, a2))
