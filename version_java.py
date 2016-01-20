#!/usr/bin/env python
#-*- encoding:UTF-8 -*-

import urllib2
import os, re

url = 'http://www.java.com/pt_BR/download/manual.jsp'
site = urllib2.urlopen(url)
html = site.readlines()

def java():
	url = 'http://www.java.com/pt_BR/download/manual.jsp' 
	site = urllib2.urlopen(url)
	html = site.readlines()
	for line in html:
		if "Version" in line:
			m = re.sub("<.*?>","",line)
			m = m.strip()
			m = re.split('[a-z]+', m, flags=re.IGNORECASE)
			versao = str(m[2]).strip()
			update = str(m[3]).strip()
	return versao, update


for line in html:
		if "Linux rpm pt JRE" in line:
			rpm = line
			break
			
rpm = str(re.split('[a-z]+', rpm, flags=re.IGNORECASE))
rpm = re.sub("[<,=,:,//,?," ",),{,},;,_,>rn,(,..'\\','\"']","",rpm)
rpm = rpm.split()

rpm = str(rpm[1])	
#print rpm

for line in html:
		if "Linux pt JRE" in line:
			tar = line
			break
			
#rpm = rpm.strip()			
tar = str(re.split('[a-z]+', tar, flags=re.IGNORECASE))
tar = re.sub("[<,=,:,//,?," ",),{,},;,_,>rn,(,..'\\','\"']","",tar)
tar = tar.split()

tar = str(tar[1])
#print tar

for line in html:
		if "Linux x64 pt JRE" in line:
			x64 = line
			break

x64 = str(re.split('[a-z]+', x64, flags=re.IGNORECASE))
x64 = re.sub("[<,=,:,//,?," ",),{,},;,_,>rn,(,..'\\','\"']","",x64)
x64 = x64.split()

x64 =  str(x64[2])

#print x64

for line in html:
		if "Linux x64-rpm pt JRE" in line:
			x64rpm = line
			break

x64rpm = str(re.split('[a-z]+', x64rpm, flags=re.IGNORECASE))
x64rpm = re.sub("[<,=,:,//,?," ",),{,},;,_,>rn,(,..'\\','\"']","",x64rpm)
x64rpm = x64rpm.split()

x64rpm = str(x64rpm[2])
#print x64rpm

#.:.
