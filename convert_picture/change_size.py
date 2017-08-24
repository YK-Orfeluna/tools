#coding:utf-8

from subprocess import getoutput
from os.path import exists, splitext, basename
import numpy as np
from cv2 import imread, resize, imwrite, INTER_AREA, INTER_CUBIC
from multiprocessing import Pool, cpu_count
from sys import argv

def run(p) :
	img = imread(p)
	h, w, c = img.shape

	h = int(np.round(h * mag, 0))
	w = int(np.round(w * mag, 0))

	out = resize(img, (w, h), interpolation=inter)

	b, e = splitext(basename(p))
	outname = outdir + "/" + b + "_R" + e
	imwrite(outname, out)
	print("resize %s" %p)


if __name__ == "__main__" :

	"""
		$1: 対象ディレクトリ
		$2: 対象ファイル拡張子
		$3: 倍率
	"""

	if len(argv) != 4 :
		exit("Error: missing args [target-dir.] [target-file's ext.] [magnification]")

	target_dir = argv[1]
	ext = argv[2]
	mag = float(argv[3])

	if target_dir[-1] == "/" :
		target_dir = target_dir[:-1]

	outdir = "%s/resize" %target_dir

	if not exists(outdir) :
		getoutput("mkdir %s" %outdir)

	if ext[0] != "." :
		ext = "." + ext

	if mag == 0 :
		exit("Error: 3rd arg(maginification) must not be ZERO")
	elif 1 <= mag :
		inter = INTER_CUBIC
	elif 0 < mag <= 1 :
		inter = INTER_AREA
	elif mag < 0 :
		mag = np.abs(1 / mag)
		inter = INTER_AREA

	
	pictures = getoutput("find %s -maxdepth 1 -type f -name '*%s'" %(target_dir, ext)).split("\n")
	pictures.sort()

	njobs = cpu_count()
	p = Pool(njobs)
	p.map(run, pictures)

	exit("done")