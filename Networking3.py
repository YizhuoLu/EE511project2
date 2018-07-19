import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from scipy.stats import binom

y=[]
G=nx.Graph()
for i in range (1, 101):
    G.add_node(i)
for i in range(1, 101):
    for j in range(i+1, 101):
            if random.random()<0.06:
                G.add_edge(i, j)
for i in range(1, 101):
    y.append(G.degree(i))
data, m, n = plt.hist(y, bins=range(0, 101), histtype='bar', edgecolor='r')
em = []
for i in range(0, 100):
    em.append(99*(binom.pmf(i, 99, 0.06)))
chisq, p = chisquare(data, em)
print("chisquare is:", chisq)
print("p value is:", p)
plt.xlabel('degree')
plt.ylabel('frequency')
plt.xlim([0, 20])
plt.show()