#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt

#create empty grapgh
G = nx.Graph()
G.add_nodes_from(["a","b","c","d"])

edge = ("a", "b")
G.add_edge(*edge)
edge = ("a", "c")
G.add_edge(*edge)

connected_list = []
for i in G.edges():
    if i[0] in G.nodes() or i[1] in G.nodes(): 
        print(f"Nodes {i} are connected")
        connected_list += i

for x in G.nodes():
    if x not in connected_list:
        print(f"Node {x} is NOT connected")

#print the graph
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

iets = []
for a, b in G.edges():
    iets.append(a)
    iets.append(b)
print(iets)
#draw the graph
nx.draw(G)
#save the graph as png
# plt.savefig("simple_path.png")
#print the graph
plt.show()