# coding: utf-8

from sys import version_info
version = version_info[0]
if version == 3 :
	from subprocess import call, check_output
else :
	exit("Sorry, this script is only supported by Python3.x.\nYour Python is not Python3.x.")

import wave, aifc
from os.path import splitext, exists, basename
from time import ctime
from platform import system


class App :
	def __init__(self, aifcname) :
		while True :
			name, ext = splitext(aifcname)
			if ext != ".aifc" and ext != ".aif" and ext != ".aiff" :
				print("Your chosen data is not AiFF.\nPlease re-input your AIFF's name.")
				aifcname = input(">>>")
			else :
				break

		self.aifcname = aifcname
		self.wavname = name +".wav"

		self.data = 0
		self.channel = 0
		self.sample_size = 0
		self.sample_rate = 0
		self.num_frame = 0

		self.bit = ""

	def read_aifc(self) :
		with aifc.open(self.aifcname, "rb") as fd :
			self.channel = fd.getchannels()				# 1=monoral, 2=stereo
			self.sample_size = fd.getsampwidth()		# sample size
			self.sample_rate = fd.getframerate()		# sampling rate
			self.num_frame = fd.getnframes()			# number of audio frame

			self.data = fd.readframes(self.num_frame)

		return 0

	def aifc2wav(self) :
		self.read_aifc()

		with wav.open(wavname, "rb") as fd :
			fd.setnchannels(self.channel)
			fd.setsampwidth(self.sample_size)
			fd.setframerate(self.sample_rate)
			fd.writeframes(self.data)

		return 0

	def convert(self) :
		self.get_info()

		cmd = ["afconvert", "-f", "WAVE", "-d", self.bit, self.aifcname, self.wavname]
		call(cmd)

		return 0

	def get_info(self) :
		cmd = ["afinfo", self.aifcname]

		info = check_output(cmd).decode("utf-8").replace(" ", "").strip().split("\n")
		d = {}

		for i in info :
			j = i.find(":")
			if j >= 0 :
				key = i[:j]
				value = i[j+1:]
				d.update({key: value})

		self.bit = d["sourcebitdepth"]

		return 0

	def main(self) :
		try :
			self.aifc2wav()
		except :
			if system() == "Darwin" :
				self.convert()
			else :
				exit("Sorry, your chosen AIFF is able to convert on MacOS X only.\nYour using OS is not MacOS X.")

		#エラーが出たら，afconvertで変換
		#問題なかったら，aifc2wav()を実行する

		print("Success!\n[%s] %s was converted to %s" %(ctime(), self.aifcname, self.wavname))

if __name__ == "__main__" :
	from sys import argv
	
	if len(argv) >= 2 :
		aifcname = argv[1]
	else :
		aifcname = "dummy"

	app = App(aifcname)
	app.main()

	exit("done")