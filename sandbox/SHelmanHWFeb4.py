#! /user/bin/python

from __future__ import division

def get_at_content(dna):
	length = len(dna)
	a_count = dna.count('A')
	t_count = dna.count ('T')
	at_content = (a_count + t_count) / length
	return at_content

my_at_content = get_at_content("ATTTGGGCCCCCTTTCCC")
print(str(my_at_content))
print(get_at_content("ATTTGGGCCCCCTTTGGG"))
print(get_at_content("aatttttcccccgggggga"))





##HOMEWORK IMPROVEMENT#
#Improve the function so it takes a new argument that sets the number of significant 
#figures & that properly treats lowercase sequences. See pg 110-111 in PFB

def get_at_contentB(dna):
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	return round (at_content, 2)
	
my_at_contentB = get_at_contentB("ATTTGGGCCCCCTTTCCC")
print(str(my_at_contentB))
print(get_at_contentB("ATTTGGGCCCCCTTTAAAGG"))
print(get_at_contentB("aatttttcccccgggggga"))




##BONUS##
def get_at_contentC(dna):
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	return round (at_content, 2)
	
my_at_contentC = get_at_contentC("TTCGNNN")
print(str(my_at_contentC))
print(get_at_contentC("tnnacgnnat"))
print(get_at_contentC("cnnnnggggccc"))   
#test, worked; no at content in last line


#NOTE : MUST HAVE FUTURE BEFORE INFDIV CHUNKS TO RUN EACH 
#IN PYTHON SEPARATELY !!! TAKEN OUT AND ADDED SHEBANG TO RUN ALL