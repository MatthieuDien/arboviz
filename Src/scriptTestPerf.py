import timeit
from tree import *
from xmlParser import xmlParser
from dotParser import dotParser
from strParser import strParser
from toAsymptote import toAsymptote
from toNetworkX import toNetworkX
from toTikZ import toTikz
import matplotlib.pyplot as plt
import sys

	
# Fonctions définissant l'exécution pour chaque type de fichier (pour les Timer)

def xml(id) :
	T=xmlParser("XML_tests/%d.xml" % id)
def dot() :
	T=dotParser("XML_tests/test.dot")
def strp() :
	T=strParser("XML_tests/test.txt")

def coord() :
	T.computeCoord()

def toasy() :
	toAsymptote(T)

def tonx() :
	toNetworkX(T)

def totikz() :
	toTikz(T)

nbNode=[]
nbNode.append(0)
execTimeXML=[]
execTimeXML.append(0)
execTimeDOT=[]
execTimeDOT.append(0)
execTimeSTR=[]
execTimeSTR.append(0)

execTimeCoord=[]
execTimeCoord.append(0)

execTimetoTikZ=[]
execTimetoTikZ.append(0)
execTimetoAsy=[]
execTimetoAsy.append(0)
execTimetoNX=[]
execTimetoNX.append(0)

nbIte=10
nbRep=3
i=1

while i<=1 :
	# Premier parsing pour récupérer la structure d'arbre
	# pour déterminer le nombre de noeuds contenu
	T=xmlParser("XML_tests/%d.xml" % i)
	nbNode.append(T.nbNode())
	
	print ('Parsing de l\'arbre %d...' % i)
	
	# Création du Timer pour le parsing XML
	test = timeit.Timer("xml(%d)"%i, "from __main__ import xml")
	execTimeXML.append(test.timeit(nbIte)/nbIte)
	
	# Création du Timer pour le parsing STR
	T.toStrFile("XML_tests/test")
	test = timeit.Timer("strp()", "from __main__ import strp")
	execTimeSTR.append(test.timeit(nbIte)/nbIte)
	
	## Création du Timer pour le parsing DOT
	#T.toDotFile("XML_tests/test")
	#test = timeit.Timer("dot()", "from __main__ import dot")
	#execTimeDOT.append(test.timeit(nbIte)/nbIte)
	
	print ('ComputeCoord pour l\'arbre %d...' % i)
	
	## Création du Timer pour computeCoord
	#test = timeit.Timer("coord()", "from __main__ import coord")
	T.computeCoord()
	
	print ('Génération de la sortie de l\'arbre %d...' % i)
	
	# Création du Timer pour TIKZ
	test = timeit.Timer("totikz()", "from __main__ import totikz")
	execTimetoTikZ.append(test.timeit(nbIte)/nbIte)
	
	# Création du Timer pour ASY
	test = timeit.Timer("toasy()", "from __main__ import toasy")
	execTimetoAsy.append(test.timeit(nbIte)/nbIte)
	
	# Création du Timer pour NX
	test = timeit.Timer("tonx()", "from __main__ import tonx")
	execTimetoNX.append(test.timeit(nbIte)/nbIte)
	
	i+=1

# Générer 3 courbes : 1 pour comparer les parsers, une pour computeCoord,
# une pour les générateurs


