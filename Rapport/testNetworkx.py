import matplotlib.pyplot as plt
import networkx as nx
import sys

nbIte = int(sys.argv[1])
longueur_arete = float(sys.argv[2])
G = nx.path_graph(nbIte)
pos={x: (5, x*longueur_arete) for x in G.nodes()}
nx.draw(G, pos, node_size=5, with_labels=False)
plt.savefig("networkx_%d_nodes.png" % nbIte)