#Accession names: Here's a list of made-up gene accession names:
#xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp
#Write a program that will print only the accession names that satisfy the following criteria:


import re   
#Allows you to use regular expressions in python
#re.search is a regular expression search (r makes it ignore special characters

names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

#Ones that contain 5
for ii in names:               #for each element ii in the string of names
    if re.search(r"5", ii):    #if you use reg expression search & find "5" in the element ii
        print(ii)              #print the element with a tab and then than element

#contain the letter d or e
for ii in names: 
    if re.search(r"(d|e)", ii):    #| means "or"
        print(ii) 

#contain the letters d and e in that order
for ii in names: 
    if re.search(r"d.*e", ii):     
        print(ii)

#contain the letters d and e in that order with a single letter between them
for ii in names: 
    if re.search(r"(d.e)", ii): 
        print(ii) 

#contain both the letters d and e in any order
for ii in names: 
    if re.search(r"d.*e", ii) or re.search(r"e.*d", ii): 
        print(ii) 

#start with x or y
for ii in names: 
    if re.search(r"^(x|y)", ii): 
        print(ii) 

#start with x or y and end with e
for ii in names: 
    if re.search(r"^(x|y).*e$", ii):       #^=starts with   $=end of line
        print(ii) 

#contain three or more numbers in a row
for ii in names: 
    if re.search(r"\d{3,}", ii):         #\d= only refers to numbers
        print(ii) 

#end with d followed by either a, r or p
for ii in names: 
    if re.search(r"d[arp]$", ii): 
        print(ii) 
