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

import xml.etree.ElementTree as etree
from tree import *

def xmlParser (src):
	"Parses a xml file into the intern tree structure"
	
	tree = etree.parse(src)
	root = tree.getroot()[0] #getRoot returns the node with the "tree" tag,
							  #we want the "node" or "leaf" inside that node
	
	return parse(root)

# Given an xml tree parsed by ElementTree, returns the corresponding Tree object
def parse(xmltree):

	if(xmltree.tag=='leaf'):
		# Case 1 : the tree is a leaf
		# Try to get the id
		l=xmltree.get('id')
		if (l):
			return Tree(label=l)
		else:
			return Tree()
	else:
		# Case 2 : the tree is a node with children
		# Get the children
		children=[]
		for child in xmltree:
			children.append(parse(child))
		# Try to get the id of the node
		l=xmltree.get('id')
		if (l):
			return Tree(label=l, children=children)
		else:
			return Tree(children=children)