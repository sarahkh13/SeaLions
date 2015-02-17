curl 'https://www.eeb.ucla.edu/seminars.php?id=[1-800]' > 1.html

!# usr/bin/python

from __future__ import division 
from bs4 import BeautifulSoup
import re 

EEBsoup = BeautifulSoup(open("2.html"))
main_content = EEBsoup.find_all(id="main-content")

my_file=open("EEB_EEP.txt")

for div in main_content: 
    panel = main_content.find("div", class_="section")
    EEB_eep = panel.strong
    if EEB_eep == "EcoEvoPub Series": 
		panel = main_content.find("div", class_="section")
    	date = panel.h4
		names = r"<p>([A-Za-z]* [A-Za-z]* ?[A-Za-z]?)<br/>" 
    	ii = re.search(names, str(panel), re.I)
    	name = ii.group(1)
	my_file.write(str(name + ", " + date + "\n"))
	
	
	
#CANT GET IT TO WORK. I WILL COME TO OFFICE HOURS
	