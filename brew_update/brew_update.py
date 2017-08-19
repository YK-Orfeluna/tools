# coding: utf-8

from sys import version_info

if version_info[0] == 2 :
	from commands import getoutput
elif version_info[0] == 3 :
	from subprocess import getoutput
else :
	exit("Error: this script operate only Python2.x or 3.x\nYour Python is not 2.x or 3.x")

print("Process: 'brew update'")
print(getoutput("brew update"))

print("Process: 'brew upgrade'")
print(getoutput("brew upgrade"))

print("Process: 'brew prune")
print(getoutput("brew prune"))

print("Process: 'brew cleanup'")
print(getoutput("brew cleanup"))

print("Process: 'brew doctor'")
print(getoutput("brew doctor"))