import os
from cryptography.fernet import Fernet

#let's find some files

files = []

for file in os.listdir():
	if file=="voldemort.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thekey.key","rb") as key:
	secertkey=key.read()


for file in files:
	with open(file, "rb")as thefile:
		contents =thefile.read()
	contents_decrypted = Fernet(secertkey).decrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_decrypted)