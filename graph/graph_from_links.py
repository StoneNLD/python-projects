#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt

#create empty grapgh
G = nx.Graph()

print(G.nodes())
print(G.edges())

print(type(G.nodes()))
print(type(G.edges()))

#adding just one node:
G.add_node("a")
# a list of nodes:
G.add_nodes_from(["b","c"])

#add edges
G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

#add other edges
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

#print the graph
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

#draw the graph
nx.draw(G)
#save the graph as png
# plt.savefig("simple_path.png")
#print the graph
plt.show()