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

from collections import defaultdict
import string

class Tree(object):
	"Local representation of tree"
	
	def __init__ (self, x = -1, depth=0, label="", children=None, offset = 0, isRoot = False):
		self.x = x
		self.y = depth
		self.label = label
		self.offset = offset
		self.height = None 
		self.width = None
		if children is None:
			self.children = list()
		else:
			self.children = children
		
	def nbNode (self):
		n=1;
		for child in self.children :
			n+=child.nbNode()
		return n
		
	def computeCoord (self):
		self.setup()
		self.addOffsets()
		return self
		
	def setup (self, depth=0, nexts=None, offset=None):
		if nexts is None:
			nexts = defaultdict(lambda:0)
		if offset is None:
			offset = defaultdict(lambda:0)
		
		# L'ordonnée est triviale, c'est la profondeur.
		self.y = depth
		
		# On calcule d'abord les coordonnées des enfants.
		for c in self.children:
			c.setup(depth+1, nexts, offset)
		
		# On centre le noeud au milieu de ses enfants.
		nbChildren = len(self.children)
		if (nbChildren == 0):
			place = nexts[depth]
			self.x = place
		else:
			place = (self.children[0].x + self.children[nbChildren-1].x) / 2
			
		# On calcule l'éventuel décalage engendré.
		offset[depth] = max(offset[depth], nexts[depth]-place)
		
		# On applique le décalage de la profondeur.
		if (nbChildren != 0):
			self.x = place + offset[depth]
			
		# On met à jour la prochaine place disponible à cette profondeur.
		nexts[depth] = self.x +1
		
		# On mémorise le décalage à appliquer au sous-arbre lors de la deuxième passe.
		self.offset = offset[depth]
		
	def addOffsets (self, offsum=0):
		self.x = self.x + offsum
		offsum = offsum + self.offset
		
		self.height = self.y
		self.width = self.x
		
		for c in self.children:
			c.addOffsets(offsum)
			self.height = max (self.height, c.height)
			self.width = max (self.width, c.width)
		
	def display(self):
		print ("(", self.label, ":", "x= ",self.x, "y= ", self.y, "off= ", self.offset, end=" ")
		for c in self.children:
			c.display()
		print (")")
		
	def toDotFile (self, fileName="treeDot"):
		f=open (fileName+".dot", "w")
		
		f.write("diagraph {")
		self.toDotFileRec(f)
		f.write("}")
		
		f.close()
		
	def toDotFileRec (self, f):
		f.write("%d[label=\""%id(self)+self.label+"\";]")
		
		for c in self.children:
			c.toDotFileRec(f)
			f.write("%d->%d;"%(id(self), id(c)))
		
	def toStrFile (self, fileName="treeStr"):
		f=open (fileName+".txt", "w")
		self.toStrFileRec(f)
		f.close()
		
	def toStrFileRec (self, f):
		f.write("("+self.label)
		for c in self.children:
			c.toStrFileRec(f)
		f.write(")")
		
	#def toXmlFile (self, fileName="treeXml"):
	
	#def toArbFile (self, fileName="treeArb"):