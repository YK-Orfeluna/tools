#coding: utf-8

from sys import argv
from time import ctime

l = len(argv)
if l == 1 :
	filename = "sample strings"
	print("[%s]\tYou did not enter your filename. This python system use sample strings." %ctime())

	txt = "We propose an acoustic AR type virtual TA agent corresponding to audience members' participating attitudes toward the lecture.\
			In one-to-many communication such as a lecture includes over 100 audiences, there are the audiences who not only paricipate toward the lecture initiatively, but also pay attention to except for the lecture.\
			In such case, it is to be desired that the lecturer corresponds the audiences will pay attention toward the lecture.  \
			However, it is not realistic from the problems such as the flow of lecture is stopped by the lecturer’s corresponding.\
			To solve such problems, we propose the acoustic AR type virtual TA agent. \
			The virtual TA agent is expressed by only moving sound field of footsteps using the parametric speaker. \
			The virtual TA agent prompts that the audiences pay attention toward the lecture by walking toward the audiences who have potential risks toward the lecturel such as they pay attention to except for the lecture. \
			As the result of experiment, the participants feel that someone exists and walks around there by perceiving the move of sound field of footsteps, and the subject of footsteps is lecturer and TA."
elif l == 2 :
	filename = argv[1]
	print("[%s]\tYour chosen file is %s" %(ctime(), filename))

	with open("sample.txt", "r") as fd :
		txt = fd.read()
else :
	exit("[%s]\tYour enterd args is missing. $python %s [filename]" %(ctime(), argv[0]))

space = " "
period = "."
n = "\n"
cnt = 0

for x, t in enumerate(txt) :
	if t == period:
		cnt += 1
	elif t == space and txt[x-1] != period and x != 0 and txt[x-1] != n and txt[x-1] != space:
		cnt += 1

print("[%s]\t'%s' has %d words." %(ctime(), filename, cnt))
