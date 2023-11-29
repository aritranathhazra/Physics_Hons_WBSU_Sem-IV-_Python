import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt

a,b = float(input("Enter the 1st boundary: ")), float(input("Enter the 2nd boundary: "))
N = int(input("Number of intermediate points: "))

x = np.linspace(a,b,N)
h = x[1]-x[0]

KE = np.zeros((N-2)**2).reshape(N-2,N-2)

for i in range(N-2):
    for j in range(N-2):
        if i==j: KE[i,j]=-2
        elif np.abs(i-j)==1: KE[i,j]=1
        
V = np.zeros((N-2)**2).reshape(N-2,N-2)
        
H = -KE/(2*h**2) + V

egnval, egnvec = np.linalg.eig(H)
z = np.argsort(egnval)
z = z[0:2]

energy = egnval[z]
print("Ground state energy eigen value = ", energy[0])
print("1st excited state energy eigen value = ", energy[1])

for i in range(len(z)):
    y = []
    y = np.append(y, -egnvec[:,z[i]])
    y = np.append(y,0)
    y = np.insert(y,0,0)
    y = y/np.sqrt(simps(abs(y) **2, x))
    if i==0: plt.plot(x,y, label = "Ground state")
    else: plt.plot(x,y, "+",label ="1st excited state")
plt.xlabel("$x$")
plt.ylabel("$\psi (x)$")
plt.legend()
plt.title("Wave functions for one dimensional infinite square well ")
plt.show()

for i in range(len(z)):
    pd = []
    pd = np.append(pd, (abs(egnvec[:,z[i]]))**2)
    pd = np.append(pd,0)
    pd = np.insert(pd,0,0)
    pd = pd/simps(pd, x)
    if i==0: plt.plot(x,pd, label = "n=1")
    else: plt.plot(x,pd, "+",label ="n=2")
plt.xlabel("$x$")
plt.ylabel("$|\psi (x)|^2$")
plt.legend()
plt.title("Probability density of ground state(n=1) and 1st excited state(n=2) \nfor one dimensional infinite square well ")
plt.show()

