
from __future__ import division
#Must include since terminal is python 2, not 3

import re

file1 = open("Vet ACE Patient Data Jan 3 07.txt").readlines()
newfile =  open("newfile.txt", "w")


for line in file1: 
	if re.search(r"SEX", line):
		print line
for line in file1: 
	if re.search(r"PATIENT NAME", line):
        print line
for line in file1: 
	if re.search(r"PATIENT ID", line):
		print line
for line in file: 
	if re.search(r"DRAWN", line):
		print line
for line in file: 
	if re.search(r"PHOS", line):
		print line
for line in file: 
	if re.search(r"BUN", line):
		print line
for line in file: 
	if re.search(r"CREAT", line):
		print line

newfile.write(str(lines))
newfile.close()
