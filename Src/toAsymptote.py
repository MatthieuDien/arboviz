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

from tree import *

def toAsymptote (t, withLabels=False, fileName="treeAsy.tex"):
	f = open (fileName, "w")
	
	f.write("\\begin{asy}\n") #LaTeX file doesn't compile if asy environment is written in the LaTeX file... strange!
	f.write("size(20cm, 20cm);\n")
	if (withLabels): # Avoid to do the test at each iteration, ever if toAsymptoteRecWith and toAsymptoteRecWithout are really similar
		toAsymptoteRecWith(t, f)
	else:
		toAsymptoteRecWithout (t, f)
	f.write("\\end{asy}\n")
	
	f.close()
	
def toAsymptoteRecWithout (t, f):
	for c in t.children:
		toAsymptoteRecWithout(c, f)
		f.write("draw((%f, -%f) -- (%f, -%f));\n" % (t.x, t.y, c.x, c.y,))

def toAsymptoteRecWith (t, f):
	f.write("label(\"%s\", (%f, -%f), E);\n" % (t.label, t.x, t.y,))
	for c in t.children:
		toAsymptoteRecWith(c, f)
		f.write("draw((%f, -%f) -- (%f, -%f));\n" % (t.x, t.y, c.x, c.y,))