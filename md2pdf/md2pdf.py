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

# making CSS to change fontsize of PDF
css = "pdf.css"
with open(css, "w") as fd :
	fd.write("body { font-size: %sem; }" %fontsize)

# checking extension of output
name, ext = splitext(output)
if ext != ".pdf" :
	output = name + ".pdf"

# run markdown-pdf
call(["markdown-pdf", "-s", css, "-o", output , markdown], shell=True)
print("[%s]: %s is wroten" %(ctime(), output))

# delete CSS
if system() == "Windows" :
	call(["del", css], shell=True)
else :
	call(["rm", css], shell=True)
	

exit("done")