# coding: utf-8

from sys import argv
from os import system
from os.path import splitext, exists
from multiprocessing import Process

def split_list (l, njobs):
	length = len(l)
	n = int(round(len(l) / njobs, 0))
	out = []
	for i in range(njobs) :
		if i != njobs-1 :
			out.append(l[n*i: (n*(i+1))])
		else :
			out.append(l[n*i: ])
	return out

def run(aicf) :
	for i in aicf :
		outname = "./convert" + splitext(i)[0] + ".wav"
		system("afconvert -f WAVE -d LEI16 %s %s" %(i, outname))

if __name__ == "__main__" :

	if not exists("./convert") :
		system("mkdir ./convert")

	njobs = argv[0]
	aicflist = agrv[1]

	with open(aicflist, "r") as f :
		aicf = f.read().split("\n")

	aicf = split_list(aicf, njobs)
	#print(aicf)

	jobs = []
	for i in range(njobs) :
		p = Process(target=run, args=(aicf[i], ))
		jobs.append(p)
		p.start()

