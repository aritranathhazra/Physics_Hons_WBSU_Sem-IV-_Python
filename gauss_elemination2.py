#Solution of equation by Gauss elemination with back substitution and 
#Determinant of coefficient matrix (Guidelines 3(a) and (c))

import numpy as np

R = int(input("Enter the number of equations:")) 

print("Enter the coefficients equationwise:") 
a=np.array([[float(input()) for i in range(R)] for j in range(R)])
p=np.copy(a)

print("Enter the r.h.s constant numbers equationwise: ")
b=np.array([float(input()) for i in range(R)])

for i in range(0,R-1):       # Determinant calculation
    for j in range(i+1,R):
        factor=p[j,i]/p[i,i]
        p[j,i:R]=p[j,i:R]-factor*p[i,i:R]

det = 1.0
for i in range(R):
    det *=p[i,i]
print("Determinant of coefficient matrix = ",det)

sol=np.zeros(shape=(R,1))

b=b.reshape(R,1)
a=np.hstack((a,b))

for i in range(0,R-1):          #elemination process
    for j in range(i+1,R):
        factor1=a[j,i]/a[i,i]
        a[j,i:R+1]=a[j,i:R+1]-factor1*a[i,i:R+1]
              
for i in range(R-1,-1,-1):
    sol[i]=(a[i,R]-np.dot(a[i,i+1:R],sol[i+1:R]))/a[i,i]
    
print("Solution of the equations:----->")
for i in range(R):
    print("X",i,"= ",sol[i])
    
