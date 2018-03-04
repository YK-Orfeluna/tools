#coding: utf-8

from sys import version_info
if version_info[0] == 3 :
	from subprocess import call
else :
	exit("Sorry, this script only supports Python3.x. Please try it again.")

from sys import argv
l = len(argv)
if l == 3 :
	markdown = argv[1]
	fontsize = argv[2]
elif l == 2 :
	markdown = argv[1]
	fontsize = 0.625
else :
	exit("Missing args. This script needs 1 or 2 args.\npython %s [$1: filename(markdown)] [$2: fontsize(em)]\n$1 is necessary to need, $2 is not nenessary to need.")

#markdown = "ntt.md"
#fontsize = 1.00

css = "pdf.css"
with open(css, "w") as fd :
	fd.write("body { font-size: %sem; }" %fontsize)


call(["markdown-pdf", "-s", css ,markdown], shell=True)

exit("done")