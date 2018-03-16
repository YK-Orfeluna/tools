#coding: utf-8

from sys import version_info
if version_info[0] == 3 :
	from subprocess import call
else :
	exit("Sorry, this script only supports Python3.x. Please try it again.")

from sys import argv
from time import ctime
from os.path import splitext
from platform import system

# check args, and set variable
l = len(argv)
if l == 4 :
	markdown = argv[1]
	fontsize = argv[2]
	output = argv[3]
elif l == 3 :
	markdown = argv[1]
	fontsize = argv[2]
	output = markdown
elif l == 2 :
	markdown = argv[1]
	fontsize = 1.0
	output = markdown
else :
	# missing args
	exit("[%s]: Missing args. This script needs 1 or 2 args.\npython %s [$1: filename(markdown)] [$2: fontsize(em)] [$3: output-name]\n$1 is necessary to need."\
		%(ctime(), argv[0]))

if system() == "Windows" :
	shell = True
else :
	shell = False

# check markdown
while True :
	name, ext = splitext(markdown)
	if ext == ".md" :
		try :
			open(markdown, "r")
			break
		except FileNotFoundError :
			markdown = input("Please input filename of markdown.\n>>>")
	else :
		markdown = input("Please input filename of markdown.\n>>>")

# check fontsize
while True :
	try :
		fontsize = float(fontsize)
		break
	except ValueError :
		fontsize = input("Please input fontsize again.\n>>>")

# making CSS to change fontsize of PDF
css = "pdf.css"
with open(css, "w") as fd :
	fd.write("body { font-size: %sem; }" %fontsize)

# checking extension of output
name, ext = splitext(output)
if ext != ".pdf" :
	output = name + ".pdf"

# run markdown-pdf
cmd = ["markdown-pdf", "-s", css, "-o", output , markdown]
call(cmd, shell=shell)
print("Success!\n[%s]: %s is converted to %s" %(ctime(), markdown, output))

# delete CSS
if system() == "Windows" :
	call(["del", css], shell=shell)
else :
	call(["rm", css], shell=shell)
	

exit("done")