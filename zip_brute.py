#!/usr/bin/env python3

import zipfile
from struct import unpack


class ZipBrute:


	def __init__(self, file_name, word_list=None):
		self.file = file_name
		self.wl = word_list


	def detect_file_type(self):

		zip_type = b"PK\x03\x04"

		with open(self.file, "rb") as f:
			header = b"".join(unpack("<4c", f.readline(4)))

			try:
				assert(header[0:4] == zip_type)

			except AssertionError:
				print("\nERROR: file is not zip\n")
				exit()


	def start_bruting(self):

		encrypted_files = list()

		with zipfile.ZipFile(self.file) as f:
			if self.wl:
				for password in self.wl:
					f.setpassword(pwd=bytes("john", "utf-8"))
					f.extractall()




def main():
	password_list = ["cat", "dog", "net", "jog", "john"]
	ZipBrute("./tests/file_wop.zip", password_list).start_bruting()



if __name__ == '__main__':
	main()