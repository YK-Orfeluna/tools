# coding: utf8

# OpenCV仕様
# RGBはBGRとして扱う
# HSVは0<=H<180, 0<=S<=100, 0<=V<=100

import numpy as np

p = 1.0 / 255.0 * 100.0

def bgr2hsv(arr, d=np.uint8) :
	B, G, R = arr

	c_max = arr.max()
	c_min = arr.min()

	V = int(round(c_max*p, 0))
	if V == 0 :
		H = 0
		S = 0

	else :
		S = 255 * (c_max - c_min) / c_max
		S = int(round(S*p, 0))


		if R == G == B :
			H = 0
		elif c_max == R :
			H = 60 * ((G - B) / (c_max - c_min))
		elif c_max == G :
			H = 60 * ((B - R) / (c_max - c_min)) + 120
		elif c_max == B :
			H = 60 * ((R - G) / (c_max - c_min)) + 240

		if H < 0 :
			H += 360
		elif H <= 360 :
			H -= 360

		H = int(round(H/2), 0)


	hsv = np.array([H, S, V], dtype=d)
	return hsv


def hsv2rgb(arr, dtype=np.uint8) :
	H, S, V = arr

	if S == 0 :
		R = V
		G = V
		B = V

	else :
		H *= 2
		S /= p
		V /= p

		c_max = V
		c_min = c_max - ((s / 255.0) * c_max)

		flag = H / 60
		if flag < 1 :
			R = c_max
			G = (H / 60.0) * (c_max - c_min) + c_min
			B = c_min
		elif flag < 2 :
			R = ((120 - H) / 60.0) * (c_max - c_min) + c_min
			G = c_max
			B = c_min
		elif flag < 3 :
			R = c_min
			G = c_max
			B = ((120 - H) / 60.0) * (c_max - c_min) + c_min
		elif flag < 4 :
			R = c_min
			G = ((240 - H) / 60.0 * (c_max - c_min)) + c_min
			B = c_max
		elif flag < 5 :
			R = ((H - 240) / 60.0) * (c_max - c_min) + c_min
			G = c_min
			B = c_max
		elif flag < 6 :
			R = c_max
			G = c_min
			B = ((360 - H) / 60.0) * (c_max - c_min) + c_min


		R = int(round(R, 0))
		G = int(round(G, 0))
		B = int(round(B, 0))

	bgr = np.array([B, G, R], dtype=d)
	return bgr
