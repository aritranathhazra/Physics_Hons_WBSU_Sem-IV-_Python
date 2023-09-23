#Largest Eigen value (Guidelines 6a)

import numpy as np 
import math as mt

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.array([1, 2, 3])

f2 = open('output.txt','w')
y=x.copy()

err=10.0
egnold=0.20
while err>0.000001:
    xold=x.copy()
    x=np.dot(a,x)
    egn=np.dot(x,y)/np.dot(xold,y)
    err=abs(egnold-egn)
    egnold=egn.copy()
x=x/mt.sqrt(np.dot(x,x))
f2.write("largest eigen value =")
f2.write(str(egn))
f2.write("\n Corresponding eigen vector is ")
f2.write(str(x))

f2.write("\n The L.H.S - R.H.S. of the secular equation = ")
f2.write(str(np.dot(a,x)-egn*x))        #varification of secular equation
f2.close()
