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

import networkx as nx
import sys
import matplotlib.pyplot as plt

node_size=5

#Main function
def toNetworkX(treeToDraw, addLabels=False, outputfile="treeNetworkX", outputformat="png") :
	if (not(treeToDraw==None)) :
		print("Generating NetworkX...")
		(G, pos) = toNetworkXrec(treeToDraw)
		print("Printing...")
		plt.clf()
		plt.gca().invert_yaxis()
		nx.draw(G, pos, with_labels=False, node_size=node_size)
		# Draw the labels a little upper, so they don't overlap the nodes
		if (addLabels):
			node_labels = nx.get_node_attributes(G,'label')
			pos_labels=dict()
			for k, v in pos.items():
				pos_labels[k]=(v[0], v[1]-0.1)
			nx.draw_networkx_labels(G, pos_labels, labels=node_labels, with_labels=True, node_size=node_size)
		plt.savefig(outputfile+'.'+outputformat)
		G.clear()
	else :
		print("Tree must not be empty.")

#Aux rec function
def toNetworkXrec(treeToDraw, pos=None) :
	if (not(pos)) :
		pos=dict()
	#create a graph and add the root and its position
	G=nx.Graph()
	G.add_node(hex(id(treeToDraw)), label=treeToDraw.label)
	pos[hex(id(treeToDraw))] = (treeToDraw.x, treeToDraw.y)
	#print("noeud courant : ",treeToDraw.label)
	#print("est une feuille ? ",(not(treeToDraw.children)))
	if (not(treeToDraw.children)) :
		#the current node is a leaf -> return the graph and the associated positions
		return (G, pos)
	else :
		for t in treeToDraw.children :
			#the current tree is not a leaf ->
			#add one edge from the root to each son, make a graph
			#from each son, and combine all the results
			#G.add_edge(treeToDraw.label, t.label)
			G.add_edge(hex(id(treeToDraw)), hex(id(t)))
			(H, pos2) = toNetworkXrec(t, pos)
			for (node, data) in H.nodes_iter(data=True):
				G.add_node(node, **data)
			G.add_edges_from(H.edges())
			pos.update(pos2)
	return (G, pos)