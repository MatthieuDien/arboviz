"""
Copyright (C) 2014 Erika Baena et Diana Malabard

This file is part of TreeDisplay.

    TreeDisplay is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    TreeDisplay is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

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
import os

	
# Fonctions définissant l'exécution pour chaque type de fichier (pour les Timer)

def xml(num) :
	if num<=1500:
		T=xmlParser("XML_tests/treeXml1To1500/tree%d.xml" % num)
	elif num<=1900:
		T=xmlParser("XML_tests/treeXml1501To1900/tree%d.xml" % num)
	elif num>=2000 and num<=30000:
		T=xmlParser("XML_tests/treeXml2000To30000/tree%d.xml" % num)
	elif num>=30100 and num<=33300:
		T=xmlParser("XML_tests/treeXml30100To33300/tree%d.xml" % num)

def dot() :
	T=dotParser("XML_tests/test.dot")
def strp() :
	T=strParser("XML_tests/test.txt")

def coord() :
	T.computeCoord()

def toasy() :
	toAsymptote(T)

def tonxpng() :
	toNetworkX(T)

def tonxpdf() :
	toNetworkX(T, outputformat="pdf")

def tonxeps() :
	toNetworkX(T, outputformat="eps")

def tonxsvg() :
	toNetworkX(T, outputformat="svg")

def totikz() :
	toTikz(T)
	
def gv() :
	cmd=os.popen("dot -Tplain -O XML_tests/test.dot")
	cmd.read()

nbNode=[]
nbNode.append(0)
nbNodeNX=[]
nbNodeNX.append(0)
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
execTimetoNXpng=[]
execTimetoNXpng.append(0)
execTimetoNXpdf=[]
execTimetoNXpdf.append(0)
execTimetoNXeps=[]
execTimetoNXeps.append(0)
execTimetoNXsvg=[]
execTimetoNXsvg.append(0)

execTimeXMLAsy=[]
execTimeXMLAsy.append(0)
execTimeGV=[]
execTimeGV.append(0)

nbIte=3
nbIteNX=5
i=1
n=0

while i<=300 and n<=200000:
	# Premier parsing pour récupérer la structure d'arbre
	# pour déterminer le nombre de noeuds contenu
	ok=True
	if i<=1500:
		T=xmlParser("XML_tests/treeXml1To1500/tree%d.xml" % i)
	elif i<=1900:
		T=xmlParser("XML_tests/treeXml1501To1900/tree%d.xml" % i)
	elif i>=2000 and i<=30000:
		T=xmlParser("XML_tests/treeXml2000To30000/tree%d.xml" % i)
	elif i>=30100 and i<=33300:
		T=xmlParser("XML_tests/treeXml30100To33300/tree%d.xml" % i)
	else:
		ok=False
	
	if ok:
		n=T.nbNode()
		# Chercher le slot où placer n
		slot=0
		while slot<len(nbNode) and nbNode[slot]<n:
			slot+=1
		nbNode.insert(slot, n)
		#slotNX=0
		#if n<=5000:
			#while slotNX<len(nbNodeNX) and nbNodeNX[slotNX]<n:
				#slotNX+=1
			#nbNodeNX.insert(slotNX, n)
			
		a=0
		b=0
		c=0
		d=0
		e=0
		f=0
		
		print ('Parsing de l\'arbre %d...' % i)
		
		# Création du Timer pour le parsing XML
		test = timeit.Timer("xml(%d)"%i, "from __main__ import xml")
		a=test.timeit(nbIte)*1000/nbIte
		execTimeXML.insert(slot, a)
		
		## Création du Timer pour le parsing STR
		#T.toStrFile("XML_tests/test")
		#test = timeit.Timer("strp()", "from __main__ import strp")
		#d=test.timeit(nbIte)*1000/nbIte
		#execTimeSTR.insert(slot, d)
		
		## Création du Timer pour le parsing DOT
		T.toDotFile("XML_tests/test")
		#test = timeit.Timer("dot()", "from __main__ import dot")
		#e=test.timeit(nbIte)*1000/nbIte
		#execTimeDOT.insert(slot, e)
		
		print ('ComputeCoord pour l\'arbre %d...' % i)
		
		#Création du Timer pour computeCoord
		test = timeit.Timer("coord()", "from __main__ import coord")
		b=test.timeit(nbIte)*1000/nbIte
		execTimeCoord.insert(slot, b)
		
		print ('Génération de la sortie de l\'arbre %d...' % i)
		
		# Création du Timer pour TIKZ
		#test = timeit.Timer("totikz()", "from __main__ import totikz")
		#execTimetoTikZ.insert(slot, test.timeit(nbIte)*1000/nbIte)
		
		# Création du Timer pour ASY
		test = timeit.Timer("toasy()", "from __main__ import toasy")
		c=test.timeit(nbIte)*1000/nbIte
		execTimetoAsy.insert(slot, c)
		
		execTimeXMLAsy.insert(slot, a+b+c)
		
		#if n<=5000:
			# Création du Timer pour NX
			#test = timeit.Timer("tonxpng()", "from __main__ import tonxpng")
			#f=test.timeit(nbIte)*1000/nbIte
			#execTimetoNXpng.insert(slotNX, f)
			#test = timeit.Timer("tonxpdf()", "from __main__ import tonxpdf")
			#execTimetoNXpdf.insert(slotNX, test.timeit(nbIteNX)*1000/nbIteNX)
			#test = timeit.Timer("tonxeps()", "from __main__ import tonxeps")
			#execTimetoNXeps.insert(slotNX, test.timeit(nbIteNX)*1000/nbIteNX)
			#test = timeit.Timer("tonxsvg()", "from __main__ import tonxsvg")
			#execTimetoNXsvg.insert(slotNX, test.timeit(nbIteNX)*1000/nbIteNX)
			
		print ('Exécution de GraphViz pour l\'arbre %d...' % i)
		
		test = timeit.Timer("gv()", "from __main__ import gv")
		execTimeGV.insert(slot, test.timeit(nbIte)*1000/nbIte)
		
		#print(("Pourcentage du tps d\'exécution pour un arbre de taille %d :\n"+
				#"meilleur cas :\n"+
				#"parser= %d ; calcul= %d ; générateur= %d\n"+
				#"pire cas :\n"+
				#"parser= %d ; calcul= %d ; générateur= %d") %
				#(n, 100*a/(a+b+c), 100*b/(a+b+c), 100*c/(a+b+c), 100*e/(e+b+f), 100*b/(e+b+f), 100*f/(e+b+f),))
		
	if i>=1900:
		i+=100
	elif i<10:
		i+=1
	else:
		i=min(1900, i+10)

# Générer 3 courbes : 1 pour comparer les parsers, une pour computeCoord,
# une pour les générateurs

#plt.figure(2)
#plt.loglog()
#plt.plot(nbNode, execTimeXML, 'b')
#plt.plot(nbNode, execTimeDOT, 'r')
#plt.plot(nbNode, execTimeSTR, 'g')
#plt.xlabel('Nombre de noeuds')
#plt.ylabel('Temps d\'exécution (ms)')
#plt.title('Temps d\'exécution des parser \n en fonction du nombre de noeuds de l\'arbre à parser')
#plt.legend(("Parser XML", "Parser DOT", "Parser STR"), 'best')
#plt.savefig("execTimeParsers.png")

#plt.figure(3)
#plt.loglog()
#plt.plot(nbNode, execTimetoAsy, 'b')
#plt.plot(nbNode, execTimetoTikZ, 'g')
#plt.xlabel('Nombre de noeuds')
#plt.ylabel('Temps d\'exécution (ms)')
#plt.title('Temps d\'exécution des générateurs Asymptote et TikZ \n'+
		  #' en fonction du nombre de noeuds de l\'arbre à afficher')
#plt.legend(("Asymptote", "TikZ"), 'best')
#plt.savefig("execTimeGenerators.png")

#plt.figure(4)
#plt.plot(nbNodeNX, execTimetoNXpng, 'r')
#plt.plot(nbNodeNX, execTimetoNXpdf, 'g')
#plt.plot(nbNodeNX, execTimetoNXeps, 'b')
#plt.plot(nbNodeNX, execTimetoNXsvg, 'm')
#plt.xlabel('Nombre de noeuds')
#plt.ylabel('Temps d\'exécution (ms)')
#plt.title('Temps d\'exécution du générateur NetworkX + Pyplot en fonction du \n'+
		  #'nombre de noeuds de l\'arbre à afficher et du type de sortie demandé')
#plt.legend(("NetworkX format PNG", "NetworkX format PDF", "NetworkX format EPS",
			#"NetworkX format SVG"), 'best')
#plt.savefig("execTimeNX.png")

#plt.figure(5)
#plt.loglog()
#plt.plot(nbNode, execTimeCoord, 'b')
#plt.xlabel('Nombre de noeuds')
#plt.ylabel('Temps d\'exécution (ms)')
#plt.title('Temps de calcul des coordonnées des noeuds \n'+
		  #' en fonction du nombre de noeuds de l\'arbre reçu en entrée')
#plt.savefig("execTimeCoord.png")

fig=plt.figure(6)
ax1 = fig.add_subplot(111)
ax2=ax1.twinx()
ax2.semilogy()
ax1.plot(nbNode, execTimeGV, 'r', label='GraphVizdfgfgsdfgsdfgsdfgsdfgsdfg')
ax2.plot(nbNode, execTimeXMLAsy, 'b', label='TreeDisplay')
plt.xlabel('Nombre de noeuds')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Comparaison entre la meilleure combinaison de \n'+
		  'TreeDisplay (XML + Asymptote) et GraphViz')
plt.legend(loc='best')
#ax1.legend(("GraphViz", "TreeDisplay (XML + Asymptote)"), 'upper left')
#ax2.legend(('TreeDisplay'), 'upper center')
plt.savefig("execTimeGV.png")
