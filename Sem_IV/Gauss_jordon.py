# Solution by Gauss Jordon method
# Determinant and Inverse of coefficient matrix (Guidelines 3(b) and (c))

import numpy as np
import sys

R=int(input("Enter the number of equations:")) 

print("Enter the coefficients equationwise:") 
a=np.array([[float(input()) for i in range(R)] for j in range(R)],dtype=float)

print("Enter the r.h.s constant numbers equationwise: ")
b=np.array([float(input()) for i in range(R)],dtype=float)

p=np.copy(a)
s=np.copy(a)
q=np.zeros(shape=(R,R))
for i in range(0,R):          #Determinant of A
    for j in range(0,R):
        if i<=2:
            factor1=p[j,i]/p[i,i]
            q[i,i:2*R+1] =factor1*p[i,i:2*R+1]
            if i!=j:
                p[j,i:2*R+1]=p[j,i:2*R+1]-q[i,i:2*R+1]
                
det = 1.0
for i in range(R):
    det *= p[i,i]
print("Determinant of the coefficient matrix = ",det)
      
b=b.reshape(R,1)
a=np.hstack((a,b))
#print(a)
c=np.zeros(shape=(R,R+1))

for i in range(0,R):          #elemination process
    for j in range(0,R):
        factor1=a[j,i]/a[i,i]
        c[i,i:R+1] =factor1*a[i,i:R+1]
        if i!=j:
            a[j,i:R+1]=a[j,i:R+1]-c[i,i:R+1]

for j in range(0,R):
    a[j,:R+1]=a[j,:R+1]/a[j,j]
#print(a)
print("Solutions of the unknown variables are:")
for i in range(R):
    print("X",i,"=",a[i,R])
    
t=np.identity(R)
s=np.hstack((s,t))
u=np.zeros(shape=(R,R+R))
for i in range(0,R+R):          #Inverse
    for j in range(0,R):
        if i<=2:
            factor1=s[j,i]/s[i,i]
            u[i,i:2*R+1] =factor1*s[i,i:2*R+1]
            if i!=j:
                s[j,i:2*R+1]=s[j,i:2*R+1]-u[i,i:2*R+1]
                
for j in range(0,R):
    s[j,:2*R+1]=s[j,:2*R+1]/s[j,j]

inv=np.zeros(shape=(R,R))
print("The inverse of coefficient matrix:")
inv[:,:]=s[:,R:2*R]
print(inv)