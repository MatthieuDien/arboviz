"""
Copyright (C) 2014 Érika Baëna et Diana Malabard

This file is part of TreeDisplay.

    TreeDisplay is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

from tree import *
from pyparsing import Word, alphas
import re

def dotParser (src):
	"Parses a dot file into the intern tree structure"
	
	f= open(src)
	
	s = f.read()
	
	(toto, i) = getWord (s, 0, '{') # [strict] (graph | diagraph) [ID]
	
	k=0
	
	# [strict]
	while (toto[k] == " "):
		k += 1
		
	if (toto[k] == 's'): #read "strict"
		if re.compile('strict').search(toto):
			if (re.search(u'strict', toto).start() != 0):
				raise Exception ("Dot syntaxe error")
			else:
				k = re.search(u'strict', toto).end()
		else:
			raise Exception ("Dot syntaxe error")
	
	# (graph|digraph)
	while (toto[k] == " "):
		k += 1
		
	if (toto[k] == 'g'): #read "graph"
		if re.compile('graph').search(toto):
			if (re.search(u'graph', toto).start() != 0):
				raise Exception ("Dot syntaxe error")
			else:
				k = re.search(u'graph', toto).end()
		else:
			raise Exception ("Dot syntaxe error")
	elif (toto[k] == 'd'): #read "diagraph"
		if re.compile('digraph').search(toto):
			if (re.search(u'digraph', toto).start() != 0):
				raise Exception ("Dot syntaxe error")
			else:
				k = re.search(u'digraph', toto).end()
		else:
			raise Exception ("Dot syntaxe error")
	else:
		raise Exception ("Dot syntaxe error")
	
	# [ID]
	while (k<i and toto[k] == " "):
		k += 1
	
	
	
	i+= 1 #skip the {
	print (s[i])
	
	dico = {}
	roots = set()
	children = set()
	
	try:
		while (True):
			(seq, i) = getWord (s, i, ';')
			seq = re.sub(r'\s', "", seq)
			j=0
			if (s[i-1] == ']'):
				# A node should be matched
				
				(num, j) = getWord(seq, j, '[')
				j += 1 # skip the '['
				
				(etiquette, j) = getWord (seq, j, '=')
				j += 1 # skip the '='
				
				(label, j) = getWord (seq, j, ']')
				j += 1 # skip the ']'

				if (num == "" or etiquette != "label" or label[0] != '\"' or label[len(label)-1] != '\"'):
					raise Exception ("Tree is ill-formed")
					
				dico[num] = Tree (label=label[1:len(label)-1])
				roots.add(dico[num])
				
			else:
				# An arrow should be matched
				
				(start, j) = getWord (seq, j, '-')
				j+=2 #skip -- or ->
				
				end = seq[j:]
				
				# Check if start and end are in dico
				t = dico[start]
				c = dico[end]
				if (t == None or c == None):
					raise Exception ("Tree is ill-formed")

				# If start not in children add to roots, add end to children
				#if t not in children:
				#	roots.add (t)
				
				if c in roots:
					roots.remove (c)
				
				children.add (c)
				#print (t, c, t.children, c.children)
				
				#Add child to node
				t.children.append(c)
				
			i+=2 # skip the ; and go to the following item		
	except IndexError:
		seq = s[i:]
		seq = re.sub(r'\s', "", seq)
		if (seq == "}"):
			# end of tree
			
			#verify that there is only one root and found it for returning
			if len(roots) != 1:
				raise Exception ("Tree is ill-formed")
			
			f.close()
			for x in roots:
				return x
			#return roots.get()
	
	#Exception indice out of array should have been raised
	f.close()
	raise Exception ("Tree is ill-formed")

def getWord (s, start, end):
	"Return a substring of s that starts at indice start and ends with caracter end excluded. Return also the indice of caracter end."
	res = ""
	j = start
	while (s[j] != end):
		res = res + s[j]
		j+=1
	return (res, j)