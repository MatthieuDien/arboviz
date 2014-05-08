import matplotlib.pyplot as plt
import networkx as nx
import sys

nbIte = int(sys.argv[1])
longueur_arete = float(sys.argv[2])
if (sys.argv[3] == "true"):
	labels = True
else:
	labels = False
filename="networkx_%d_nodes" % (nbIte,)
if (labels):
	filename += "A.png"
else:
	filename += "B.png"
G = nx.path_graph(nbIte)
pos={x: (5, x*longueur_arete) for x in G.nodes()}
if (labels):
	labels={x: "label" for x in G.nodes()}
	nx.draw(G, pos, labels=labels, node_size=5, with_labels=True)
else:
	nx.draw(G, pos, node_size=5, with_labels=False)
plt.savefig(filename)