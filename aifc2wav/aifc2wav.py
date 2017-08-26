# coding: utf-8

from subprocess import getoutput
from os.path import splitext, exists, basename
from time import ctime

def run(aicf) :
	outname = outdir + "/" + basename(splitext(aicf)[0]) + ".wav"

	getoutput("afconvert -f WAVE -d LEI16 %s %s" %(aicf, outname))

	print("[%s]\ndone: convert to wav-file: %s" %(ctime, aicf))

if __name__ == "__main__" :
	from sys import argv
	from multiprocessing import Pool, cpu_count

	target_dir = agrv[1]

	if target_dir[-1] == "/" :
		target_dir = target_dir[: -1]

	aicflist = getoutput("find %s -maxdepth 1 -mindepth 1 -type f -name '*.aicf'" \
		%target_dir).split("\n")
	aicflist.sort()

	outdir = "%s/convert" %target_dir
	if not exists(outdir) :
		getoutput("mkdir %s" %outdir)

	print("[%s]\ndone: read aicf-files" %ctime())

	njobs = cpu_count()
	p = Pool(njobs)
	p.map(run, aicflist)

	exit("done")

	

