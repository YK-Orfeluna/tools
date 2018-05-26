#coding: utf-8

from sys import version_info
if version_info[0] == 3 :
	from subprocess import call
else :
	exit("Sorry, this script only supports Python3.x. Please try it again.")

from time import ctime
from os.path import splitext
from platform import system
OS = system()

class App :

	def __init__(self, markdown, fontsize=1, pdf="") :
		self.markdown = markdown
		self.fontsize = fontsize
		self.pdf = pdf

		if OS == "Windows" :
			self.flag = True
		else :
			self.flag = False

		self.css = "pdf.css"

	def check_names(self) :
		self.check_md()
		self.check_fontsize()
		self.check_pdf()

	def check_md(self) :
		# check markdown
		while True :
			name, ext = splitext(self.markdown)
			if ext == ".md" :
				try :
					fd = open(self.markdown, "r")
					fd.close()
					break
				except FileNotFoundError :
					self.markdown = input("Please input filename of markdown.\n>>>")
			else :
				self.markdown = input("Please input filename of markdown.\n>>>")

	def check_pdf(self) :
		if self.pdf == "" :
			self.pdf = splitext(self.markdown)[0] + ".pdf"
		else :
			while True :
				name , ext = splitext(self.pdf)
				if ext == ".pdf" :
					break
				elif ext == ".md" :
					self.pdf = name + ".pdf"
				else :
					self.pdf = input("Please re-input output filename (PDF).\n>>>")

	def check_fontsize(self) :
		# check fontsize
		while True :
			try :
				self.fontsize = float(self.fontsize)
				break
			except ValueError :
				self.fontsize = input("Please input fontsize again.\n>>>")

	def convert(self) :
		# run markdown-pdf
		self.make_css()
		cmd = ["markdown-pdf", "-s", self.css, "-o", self.pdf , self.markdown]
		call(cmd, shell=self.flag)
		print("Success!\n[%s]: %s is converted to %s" %(ctime(), self.markdown, self.pdf))
		self.rm_css()

	def make_css(self) :
		# making CSS to change fontsize of PDF
		with open(self.css, "w") as fd :
			fd.write("body { font-size: %sem; }" %self.fontsize)

	def rm_css(self) :
		if OS == "Windows" :
			cmd = ["del", self.css]
		else :
			cmd = ["rm", self.css]

		call(cmd, shell=self.flag)

	def main(self) :
		self.check_names()
		self.convert()

def __button1() :
	global markdown



if __name__ == "__main__" :
	from tkinter import Tk, ttk, messagebox, filedialog

	fType = [("markdown", "*.md")]
	markdown = filedialog.askopenfilename(title="Choose your Markdown-file", filetypes=fType)

	if markdown == "" :
		exit("done")

	# フォントサイズを選ぶ

	# 出力先とファイル名を選ぶ

	# 実行







	"""
	from sys import argv
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

	app = App(markdown, fontsize, output)
	app.main()
	"""

	exit("done")