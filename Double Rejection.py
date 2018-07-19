from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt

def Bpdf(t, a, b):
    f = gamma(a+b)/(gamma(a)*gamma(b))
    return f*(t**(a-1))*((1-t)**(b-1))
x = np.linspace(0, 1, 100)
print('firt max is:', np.max(0.5*Bpdf(x, 8, 5)))
def g(x):
    if 0< x <= 1:
        return 1.47 * 1
    elif 4 < x <= 6:
        return 1/(6-4)
    else:
        return 0
h=[]
x = np.arange(0, 8, 0.1)
for i in x:
    h.append(g(i))
plt.figure(2)
plt.plot(x, h)
plt.title('g(x)')
plt.xlabel('x')
plt.ylabel('g(x)')
def f(x):
    if 0 < x <= 1:
        return 0.5*Bpdf(x, 8, 5)
    elif 4 < x <= 5:
        return 0.5*(x-4)
    elif 5 < x <= 6:
        return -0.5*(x-6)
    else:
        return 0
y=[]
x = np.arange(0, 8.0, 0.1)
for i in x:
    y.append(f(i))
plt.figure(1)
plt.plot(x, y)
plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
c = 1.47/1.463
rejection = 0
for i in range(0, 1000):
    u = np.random.uniform(0, 1)
    xcard = np.random.uniform(0, 6)
    if g(xcard)==0:
        continue
    elif u > (f(xcard)/(c*g(xcard))):
        rejection += 1
    else:
        continue
rate = rejection/1000
print('The rejection rate is:', rate)
plt.show()