import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import chisquare
import math

count = []
for i in range(1, 1001):
    sum = 0
    for j in range(0, 1000):
        if sum > 1:
            count.append(j-1)
            break
        else:
            sum += ((-1 / 5) * np.log(1 - random.random()))
def Poisson_pmf(L, k):
    return (L**k*math.exp(-L))/math.factorial(k)
data, m, n = plt.hist(count, bins=np.arange(0, 15, 1), histtype='bar', edgecolor='r')
plt.xlabel('the number of samples that occur in 1 time interval')
plt.ylabel('frequency')
em = []
for i in range(0, 14):
    em.append(1000*Poisson_pmf(5, i))
chisq, p = chisquare(data, em)
print("chisquare is:", chisq)
print("P value is:", p)
plt.show()
