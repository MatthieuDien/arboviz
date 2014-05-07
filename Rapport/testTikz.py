import sys

nbIte = int(sys.argv[1])
if (sys.argv[2] == "true"):
	labels = True
else:
	labels = False
i = 0

fileName = "testTikz%d" % (nbIte,)

if (labels):
	fileName += "A.tex"
else:
	fileName += "B.tex"

fichierTest = open (fileName, "w")

if (labels):
	fichierTest.write("\\node (a%d) at (0,%d) {$%d$};\n" % (i, i, i,))
	i += 1
	while i<nbIte:
		fichierTest.write ("\\node (a%d) at (0,%d) {$%d$};\n" % (i, i, i,))
		fichierTest.write ("\\draw (a%d) -- (a%d);\n" % (i-1, i,))
		i += 1
else:
	i += 1
	while i<nbIte:
		fichierTest.write ("\\draw (0,%d) -- (0,%d);\n" % (i-1, i,))
		i += 1

fichierTest.close()
