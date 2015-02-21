#! /usr/bin/python

from __future__ import division

import re







#Set input file name
InFileName = 'Vet ACE Patient Data Jan 3 07.txt'

#Open the input file
InFile = open(InFileName, 'r').readlines()

#Output file 
OutFile =  open("newfile.txt", "w")

#Initialize the counter used to keep track of line numbers
LineNumber = 0 

#Loop over each line in the file
for line in InFile: 
	line = line.strip('\n')           #Remove the line ending characters
	ElementList = line.split('\t')    ## Split the line into a list of ElementList, with tab delimiters
	
	#Isolate the stuff I want
	SearchStr = '(SEX:*\n)(PATIENT NAME:.*\n)(PATIENT ID:.*\n)(D/T DRAWN:.*\n)(D/T DRAWN:.*\n)(PHOS:.*\n)(BUN:.*\n)(CREA:.*\n)'
	Result = re.search(SearchStr, ElementList)
	
	#Get the captured character groups from the search
	sex = float(Result.group(1))
	name = float(Result.group(2))
	ID = float(Result.group(3))
	date = float(Result.group(4))
	phos = float(Result.group(5))
	bun = float(Result.group(6))
	crea = float(Result.group(7))
	#print sex + name + ID + date + phos + bun + crea

OutFile.write(str(sex + name + ID + date + phos + BUN + CRE))
OutFile.close()


