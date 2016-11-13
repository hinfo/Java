#!/usr/bin/env python
#-*- encoding:UTF-8 -*-

import os
from version_java import *

"""
Funções para auxiliar na instalação do java
"""

def install_debian():
		'''
		Instala java em deriados do Debian
		'''
		print "Adicionando o ppa:webupd8team/java"
		os.system('sudo add-apt-repository ppa:webupd8team/java')
		print "Atualizando os pacotes"
		os.system('sudo apt-get update')
		print "Instalando o Java"
		os.sytem('sudo apt-get install oracle-java8-installer')
		os.system('sudo update-java-alternatives -s java-8-oracle')
		os.system('sudo apt-get install oracle-java8-set-default')
		os.system('java -version')
	
def install_rpm(f_rpm):
		'''
		Instala no modo rpm
		'''
		print "Instalando o Java..."
		os.system('sudo rpm -ivh %s' % f_rpm)
		os.system('sudo rm %s' % f_rpm)
		
def install_tar(f_tar):
		'''
		Instalar usando arquivo tar.gz
		'''
		print "Instalando o Java..."
		versao = java()[0]
		update = java()[1]
		dirtmp = "jre1.%s.0_%s" % (versao,update)
		os.system('chmod +x %s' % f_tar)
		os.system('tar xavf %s' % f_tar)
		os.system('mv %s /usr/lib/java/' % dirtmp)
		os.system('rm %s' % f_tar)
		
		
#.:.
