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

nbIte=10
i=1

while i<=33300 :
#while i<=50 :
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
		#nbNode.append(n)
		# Chercher le slot où placer n
		slot=0
		while slot<len(nbNode) and nbNode[slot]<n:
			slot+=1
			#if nbNode[slot]!=n:
		nbNode.insert(slot, n)
		slotNX=0
		if n<=30:
			#nbNodeNX.append(n)
			while slotNX<len(nbNodeNX) and nbNodeNX[slotNX]<n:
				slotNX+=1
			#if slotNX==len(nbNodeNX) or [slotNX]!=n:
			nbNodeNX.insert(slotNX, n)
		
		print ('Parsing de l\'arbre %d...' % i)
		
		# Création du Timer pour le parsing XML
		test = timeit.Timer("xml(%d)"%i, "from __main__ import xml")
		execTimeXML.insert(slot, test.timeit(nbIte)/nbIte)
		
		# Création du Timer pour le parsing STR
		T.toStrFile("XML_tests/test")
		test = timeit.Timer("strp()", "from __main__ import strp")
		execTimeSTR.insert(slot, test.timeit(nbIte)/nbIte)
		
		# Création du Timer pour le parsing DOT
		T.toDotFile("XML_tests/test")
		test = timeit.Timer("dot()", "from __main__ import dot")
		execTimeDOT.insert(slot, test.timeit(nbIte)/nbIte)
		
		print ('ComputeCoord pour l\'arbre %d...' % i)
		
		# Création du Timer pour computeCoord
		test = timeit.Timer("coord()", "from __main__ import coord")
		execTimeCoord.insert(slot, test.timeit(nbIte)/nbIte)
		
		print ('Génération de la sortie de l\'arbre %d...' % i)
		
		# Création du Timer pour TIKZ
		test = timeit.Timer("totikz()", "from __main__ import totikz")
		execTimetoTikZ.insert(slot, test.timeit(nbIte)/nbIte)
		
		# Création du Timer pour ASY
		test = timeit.Timer("toasy()", "from __main__ import toasy")
		execTimetoAsy.insert(slot, test.timeit(nbIte)/nbIte)
		
		if n<=30:
			# Création du Timer pour NX
			test = timeit.Timer("tonxpng()", "from __main__ import tonxpng")
			execTimetoNXpng.insert(slotNX, test.timeit(nbIte)/nbIte)
			test = timeit.Timer("tonxpdf()", "from __main__ import tonxpdf")
			execTimetoNXpdf.insert(slotNX, test.timeit(nbIte)/nbIte)
			test = timeit.Timer("tonxeps()", "from __main__ import tonxeps")
			execTimetoNXeps.insert(slotNX, test.timeit(nbIte)/nbIte)
			test = timeit.Timer("tonxsvg()", "from __main__ import tonxsvg")
			execTimetoNXsvg.insert(slotNX, test.timeit(nbIte)/nbIte)
		
	i+=1

# Générer 3 courbes : 1 pour comparer les parsers, une pour computeCoord,
# une pour les générateurs

plt.figure(2)
plt.plot(nbNode, execTimeXML, 'b')
plt.plot(nbNode, execTimeDOT, 'r')
plt.plot(nbNode, execTimeSTR, 'g')
plt.xlabel('Nombre de noeuds')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Temps d\'exécution des parser \n en fonction du nombre de noeuds de l\'arbre à parser')
plt.legend(("Parser XML", "Parser DOT", "Parser STR"), 'best')
plt.savefig("execTimeParsers.png")

plt.figure(3)
plt.plot(nbNode, execTimetoAsy, 'b')
plt.plot(nbNode, execTimetoTikZ, 'g')
plt.xlabel('Nombre de noeuds')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Temps d\'exécution des générateurs Asymptote et TikZ \n'+
		  ' en fonction du nombre de noeuds de l\'arbre à afficher')
plt.legend(("Asymptote", "TikZ"), 'best')
plt.savefig("execTimeGenerators.png")

plt.figure(4)
plt.plot(nbNodeNX, execTimetoNXpng, 'r')
plt.plot(nbNodeNX, execTimetoNXpdf, 'g')
plt.plot(nbNodeNX, execTimetoNXeps, 'b')
plt.plot(nbNodeNX, execTimetoNXsvg, 'm')
plt.xlabel('Nombre de noeuds')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Temps d\'exécution du générateur NetworkX \n '+
		  'en fonction du nombre de noeuds de l\'arbre à afficher \n'+
		  ' et du type de sortie demandé')
plt.legend(("NetworkX format PNG", "NetworkX format PDF", "NetworkX format EPS",
			"NetworkX format SVG"), 'best')
plt.savefig("execTimeNX.png")

plt.figure(5)
plt.plot(nbNode, execTimeCoord, 'b')
plt.xlabel('Nombre de noeuds')
plt.ylabel('Temps d\'exécution (ms)')
plt.title('Temps de calcul des coordonnées des noeuds \n'+
		  ' en fonction du nombre de noeuds de l\'arbre reçu en entrée')
plt.savefig("execTimeCoord.png")
