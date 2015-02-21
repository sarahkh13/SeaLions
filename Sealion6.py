
from __future__ import division
#Must include since terminal is python 2, not 3

import re

file1 = open("Vet ACE Patient Data Jan 3 07.txt").readlines()
newfile =  open("newfile.txt", "w")

for line in file1: 
	sex = re.search(r"SEX", line)
	name = re.search(r"PATIENT NAME", line)
	ID = re.search(r"PATIENT ID", line)
	date = re.search(r"DRAWN", line)
	phos = re.search(r"PHOS", line)
	BUN = re.search(r"BUN", line)
	CRE = re.search(r"CREAT", line)

print(str("sex" + "name" + "ID" + "date" + "phos" + "BUN" + "CRE"))
#print(str(sex + name + ID + date + phos + BUN + CRE))
#newfile.write(str("sex" + "name" + "ID" + "date" + "phos" + "BUN" + "CRE"))
newfile.write(str(sex + name + ID + date + phos + BUN + CRE))
newfile.close()
