#!/usr/bin/env python
#*-* encoding: UTF-8 *-*

# ****************************
#   Download java for Linux
#     Ver 1.0 By Hinfo
#*****************************

import urllib2, urllib, os
from install_java import *
from version_java import *

# Site contendo os arquivos para Download
url = 'http://www.java.com/inc/BrowserRedirect1.jsp?locale=pt_BR'

# A seguir é acessado o site e realizado uma leitura 
site = urllib2.urlopen(url)
html = site.readlines()

#Versão do Java
versao = java()[0]
update = java()[1]

'''
#link para baixar o JDK 8u66
http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-i586.rpm
http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-i586.tar.gz
http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.rpm
http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz

'''
print
print """ 
*****************************************************
              DOWNLOAD AND INSTALL JAVA FOR LINUX
                  ver 1.0 by Hinfo
*****************************************************
"""

print "Java Versão %s update %s" % (versao, update)
print("""Escolha uma das opções:
	1 - Linux RPM (Red Hat, Fedora e derivados)
	2 - Linux i386(586/686) (Arquivo tar | Versão para extração e instalação no braço)
	3 - Linux 64 RPM (Red Hat, Fedora e derivados 64 bits)
	4 - Linux 64 (Arquivo tar 64 bits| Versão para extração e instalação no braço)
	5 - Não tem versão para Debian/Ubuntu?
	""" )

# Espera-se que escolha uma das alternativas.
# Versão 2.0 terá validade de entrada, vá que alguém não saiba ler, :)

choice = int(raw_input('Opção: '))


#Define a versão a ser instalada
if choice == 1:
	file_java = "java-linux-i586.rpm"
	version = rpm
	mode = 'rpm'
elif choice == 2:
	file_java = "java-linux-i586.tar.gz"
	version = tar
	mode = 'tar'
elif choice == 3:
	file_java = "java-linux-64.rpm"
	version = x64rpm
	mode = 'rpm'
elif choice == 4:
	file_java = "java-linux-64.tar.gz"
	version = x64
	mode = 'tar'
elif choice == 5:
	# Para os derivados de Debian/Ubuntu
	print "Tem sim." 
	mode = 'debian'

else:
	print "Nenhuma de suas escolhas satifaz o menu!"


#Versão escolhida, hands on.
cont = 0
if choice > 0 and choice < 5:
	for line in html:
		if version in line:
			cont = cont + 1
			break
	print "Encontrado %s ocorrência(s)" %cont
	url2 = "http://javadl.sun.com/webapps/download/AutoDL?BundleId="+version
	print "Baixando arquivo: "+file_java+" ...."
	download = urllib.urlretrieve(url2, file_java)  
	print "Download Concluído"

else: 
	print "Vamos instalar o java!"
	

debian = """
	Digite no terminal como root:
		# add-apt-repository ppa:webupd8team/java
		# apt-get update
		# apt-get install oracle-java8-installer
		# update-java-alternatives -s java-8-oracle 
		# apt-get install oracle-java8-set-default (Configura variaveis de Ambiente)
	"""

"""
if mode == 'rpm':
	install_rpm(file_java)
	
elif mode == 'tar':
	install_tar(file_java)
	
else:
	install_debian()
"""
os.system('java -version')

print ".:.       \m/       .:."

#Finish .:.