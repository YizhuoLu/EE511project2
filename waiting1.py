import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import chisquare
import math

X=[]
for i in range(1, 1001):
    X.append((-1/5)*np.log(1-random.random()))
print(X)
data, m, n = plt.hist(X, bins=np.arange(0,3.1,0.1), histtype='bar', edgecolor='r')
plt.xlabel('Xi')
plt.ylabel('frequency')
def expcdf(x):
    return (1-math.exp(-5*x))
em = []
for i in range(0, 30):
    em.append(1000*(expcdf((i+1)/10)-expcdf(i/10)))
chisq, p = chisquare(data, em)
print("chisquare is:", chisq)
print("P value is:", p)
plt.show()