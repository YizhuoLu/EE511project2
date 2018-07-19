import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

y=[]
G=nx.Graph()
for i in range(1, 51):
    G.add_node(i)
for i in range(1, 51):
    for j in range(i+1, 51):
        if random.random()<0.09:
            G.add_edge(i, j)
for i in range(1, 51):
    y.append(G.degree(i))
plt.hist(y, bins=range(0, 51), histtype='bar', edgecolor='r')
plt.xlabel('degree')
plt.ylabel('frequency')
plt.xlim([0,10])
plt.show()