#! /usr/bin/python

from __future__ import division

import re

file1 = open("Vet ACE Patient Data Jan 3 07.txt").readlines()
newfile =  open("newfile.txt", "w")
#New Attempt: 
def sealions(SLText): 
	SearchStr = '(SEX.*\n)(PATIENT NAME:.*\n)(PATIENT ID:.*\n)(D/T DRAWN:.*\n)(D/T DRAWN:.*\n)(PHOS:.*\n)(BUN:.*\n)(CREA:.*\n)'
	Result = re.search(SearchStr, SLText)
	
	#Get the captured character groups from the search
	sex = float(Result.group(1))
	name = float(Result.group(2))
	ID = float(Result.group(3))
	date = float(Result.group(4))
	phos = float(Result.group(5))
	bun = float(Result.group(6))
	crea = float(Result.group(7))

	return = sex + name + ID + date + phos + bun + crea
	break


newfile.write(sealion_data)
newfile.close()
