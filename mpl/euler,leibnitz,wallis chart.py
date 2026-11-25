def leibnitz(n):
    L=[]
    X=[]
    Z=[]
    s=0
    pi = 0.0
    sign = -1

    for i in range(1,n+1):
        s = s + 1.0*(-1)**(i+1)*4/(2*i-1)
        X.append(i)
        L.append(round(s,2))
        Z.append(3.14)
    return X, L, Z

import math

def euler(n):
    pi = 0.0
    E = []

    for i in range(1, n + 1):
        pi += 1.0 / (i * i)
        E.append(math.sqrt(6 * pi))

    return E

def wallis(n):
    pi = 1.0
    W = []

    for i in range(1, n + 1):
        pi *= (2.0 * i) / (2.0 * i - 1) * (2.0 * i) / (2.0 * i + 1)
        W.append(pi * 2)

    return W

rep = 50
X, L, Z = leibnitz(rep)
E = euler(rep)
W = wallis(rep)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig,ax = plt.subplots()
ax.plot(L, c='red', label="Leibnitz")
ax.plot(Z, c='black', label="Pi")
ax.plot(E, c='blue', label="Euler")
ax.plot(W, c='yellow', label="Wallis")
ax.set_title("Approaching to number PI", fontsize=12, c='black')
ax.set_xlabel("Number of iterations", fontsize=12 )
ax.set_ylabel("Calculated Value of PI", fontsize=12)
ax.legend(bbox_to_anchor=(1,1), ncol=4)
plt.tight_layout()
plt.show()