# coding: utf-8

from sys import version_info
version = version_info[0]
if version == 3 :
	from subprocess import call
else :
	exit("Sorry, this script is only supported by Python3.x.\nYour Python is not Python3.x.")

import wave, aifc
from os.path import splitext, exists, basename
from time import ctime


class App :
	def __init__(self, aifcname) :
		while True :
			name, ext = splitext(aifcname)
			if ext == ".aifc" or ext == ".aif" or ext == ".aiff" :
				print("Your chosen data is not AiFF.\nPlease re-input your data-name.")
				aifcname = input(">>>")
			else :
				break

		self.aifcname = aifcname
		self.wavname = name +".wav"

	def read_aifc(self) :
		with aifc.open(self.aifcname, "rb") as fd :
			self.data = fd.read()
			self.channel = fd.getchannels()				# 1=monoral, 2=stereo
			self.sample_size = fd.getsampwidth()		# sample size
			self.sample_rate = fd.getframerate()		# sampling rate
			self.num_frame = fd.getnframes()			# number of audio frame

		return 0

	def aifc2wav(self) :
		with wav.open(wavname, "rb") as fd :
			fd.setnchannels(self.channel)
			fd.setsampwidth(self.sample_size)
			fd.setframerate(self.sample_rate)
			fd.writeframes(self.data)

		return 0

	def convert(self) :
		command = ["afconvert", "-f", "WAVE", "-d", "LEI16", self.aifcname, self.wavname]
		call(command, shell=True)

		return 0

	def main(self) :
		try :
			self.read_aifc()
		error 
		#エラーが出たら，afconvertで変換
		#問題なかったら，aifc2wav()を実行する

		print("[%s] %s was converted to %s" %(ctime(), self.aifcname, self.wavname))

if __name__ == "__main__" :
	from sys import argv
	
	if len(argv) > 2 :
		argv[1] = aifcname
	else :
		"dummy"

	app = App(aifcname)
	app.main()

	exit("done")