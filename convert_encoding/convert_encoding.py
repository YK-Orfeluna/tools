#coding: utf-8

from sys import version_info, argv
from time import ctime

# check commandline-arg
l = len(argv)
if l != 2 :
	exit("[%s]\tThere are missing args. $python %s [dir_name]" %(ctime(), argv[0]))

# check version of python
if version_info[0] == 2 :
	from commands import getoutput
elif version_info[0] == 3 :
	from subprocess import getoutput
else :
	exit("Error: this script operate only Python2.x or 3.x\nYour Python is not 2.x or 3.x")


# To convert to utf-8 using nkf
dir_name = argv[1]
if dir_name[-1] == "/" :
	dir_name = dir_name[: -1]
getoutput("find %s -type f -exec nkf --overwrite -w {} \;" %dir_name)

exit("[%s]\tdone: All files in [%s] are converted to 'UTF-8'" %(ctime(), dir_name))