import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

G=nx.Graph()
for i in range(1, 51):
    G.add_node(i)
for i in range(1, 51):
    for j in range(i+1, 51):
        if random.random()<0.12:
            G.add_edge(i, j)
nx.draw(G, pos=nx.random_layout(G), node_size=100, nodecolor='r', edge_color='b')
plt.show()