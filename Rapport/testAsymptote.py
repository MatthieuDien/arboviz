import sys

nbIte = int(sys.argv[1])
if (sys.argv[2] == "true"):
	labels = True
else:
	labels = False

i = 0

fileName = "testAsymptote%d" % (nbIte,)
if (labels):
	fileName += "A.tex"
else:
	fileName += "B.tex"

fichierTest = open (fileName, "w")
fichierTest.write("\\begin{asy}\n")
fichierTest.write("size(20cm,20cm);\n")

if (labels):
	fichierTest.write("label(\"a%d\", (0, %d), E);\n" % (i, i,))
	
i += 1

while i<nbIte:
	if (labels):
		fichierTest.write ("label(\"a%d\", (0, %d), E);\n" % (i, i,))
	fichierTest.write ("draw((0, %d) -- (0, %d));\n" % ((i-1), i,))
	i += 1
	
fichierTest.write("\\end{asy}\n")

fichierTest.close()
