# -*- coding: utf-8 -*

from sys import argv
from os.path import splitext
import qrcode

if __name__ == "__main__" :

	if len(argv) == 3 :
		url = argv[1]
		name = argv[2]
	else :
		exit("$1: URL, $2: QR-image's name")

	if splitext(name)[1] == "" :
		name += ".png"

	img = qrcode.make(url)
	img.show()
	img.save(name)

	print("converted\n%s\nto\n%s" %(url, name))
	exit()