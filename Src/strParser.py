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
import re

nbCharAlire = 1024

def strParser (src):
	"Parses a string file into the intern tree structure"

	f=open(src, 'r')
	s=f.read(nbCharAlire)
	#(T, f) = parse(f, f.read(1))
	T=parse(f, s)[0]
	f.close()

	return T

def parse (f, s, currentIndex=0):

	isWhiteSpace=re.compile("[\s]")

	(f, s, currentIndex) = skipSpaces(f, s, currentIndex)

	if s[currentIndex]!='(':
		raise Exception ("The tree is ill-formed : A tree should start with a '('")

	(f, s, currentIndex) = incrementIndex(f, s, currentIndex)
	size = len(s)
	c = s[currentIndex]
	label=""

	(f, s, currentIndex) = skipSpaces(f, s, currentIndex)
	if (s==[]):
		raise Exception ("The tree is ill-formed : End of file reached")
	c = s[currentIndex]

	while (s!=[] and c!='(' and c != ')'):
		#print("currentIndex=",currentIndex)
		if (not isWhiteSpace.match(c)):
			label = label + c
		(f, s, currentIndex) = incrementIndex(f, s, currentIndex)
		c = s[currentIndex]

	(f, s, currentIndex) = skipSpaces(f, s, currentIndex)
	c = s[currentIndex]

	listChildren = []
	while (s!=[] and c == '('):
		(child, s, currentIndex) = parse (f, s, currentIndex)
		listChildren.append(child)
		#print("fils ",label,"ajouté")
		(f, s, currentIndex) = skipSpaces(f, s, currentIndex)
		c = s[currentIndex]
		#print("c après avoir ajouté le fils",label,": ",c)

	(f, s, currentIndex) = skipSpaces(f, s, currentIndex)
	c = s[currentIndex]
	if (c == ')'):
		(f, s, currentIndex) = incrementIndex(f, s, currentIndex)
		return (Tree(label = label, children=listChildren), s, currentIndex)
	else:
		raise Exception ("The tree is ill-formed : The tree",label,"should end with a ')'")

def incrementIndex(f, s, currentIndex):
	currentIndex+=1
	l=len(s)
	if (currentIndex>=l):
		#print("fin du buffer -> on re-remplit")
		s=f.read(nbCharAlire)
		currentIndex=0
	if (s==[]):
		raise Exception ("The tree is ill-formed : End of file reached")
	#print("currentIndex dans incrementIndex :",currentIndex)
	return (f, s, currentIndex)

def skipSpaces(f, s, currentIndex) :
	isWhiteSpace=re.compile("[\s]")
	while (s!=[] and isWhiteSpace.match(s[currentIndex])):
		(f, s, currentIndex) = incrementIndex(f, s, currentIndex)
	return (f, s, currentIndex)