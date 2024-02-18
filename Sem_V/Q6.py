#  Q6  probability for position of electron in H atom
import math as mt

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as intg
import scipy.special as sc


def sprcl(l,m,theta):
    if(m<0.0): m = abs(m)
    Y_lm = (-1)**m *np.sqrt((2*l+1.)*mt.factorial(l-m)/(4.*np.pi*mt.factorial(l+m)))
    Y_lm = Y_lm * sc.lpmn(m,l,np.cos(theta))[0][m,l]
    return Y_lm

def radial(n,l,x):
    R_nl = mt.factorial(n+l)*mt.exp(-x/n) *(2*x/n)**l *sc.assoc_laguerre(2*x/n,n-l-1,2*l+1)
    R_nl = R_nl * np.sqrt((2/n)**3 *mt.factorial(n-l-1)/((2*n)*mt.factorial(n+l)**3))
    return R_nl

points = 1000
div1 = np.pi/(points-1)
angle = np.arange(0, np.pi, div1)
angle2 = np.arange(np.pi, 2*np.pi, div1)
div2 = 1/(points-1)
rad = np.arange(0, 100, div2)
pol = np.arange(0, 2*np.pi, 2*div1)

for i in range(1,3):        #i-->n
    for j in range(0,i):        #j-->l
        for k in range(-j,j+1):     #k-->m
            for a in range(1,3):        #a-->n_prime
                for b in range(0,a):        #b-->l_prime
                    for c in range(-b,b+1):     #c-->m_prime
                        
                        s_h = [sprcl(j,k,th)*sprcl(b,c,th)*np.sin(th) for th in angle]
                        r = [radial(i,j,radius)*radial(a,b,radius)*radius**2 for radius in rad]
                        az1 = intg.quad(lambda phi: np.sin((k-c)*phi), 0, 2*np.pi)[0]
                        az2 = intg.quad(lambda phi: np.cos((k-c)*phi), 0, 2*np.pi)[0]
                        az = np.sqrt(az1**2 +az2**2)
                        integration = intg.simps(s_h,angle)*intg.simps(r, rad)*az
                        if (i==1 and a==1 and j==0 and b==0 and k==0 and c==0):
                             plt.polar(angle, s_h,"g.")
                             plt.title("Angular probability density distribution for ground state")
                             plt.figtext(0.0,-0.1, "Note: Here the value of \u03B8 runs from 0 to \u03C0 which are the limits of the integration \n for finding the total angular probability distribution.")
                             plt.show()
                             s_h2 = [sprcl(j,k,th)*sprcl(b,c,th)*abs(np.sin(th)) for th in angle2]
                             s = np.append(s_h, s_h2)
                             ang = np.append(angle, angle2)
                             plt.polar(ang, s,"g.")
                             plt.title("Angular probability density distribution for ground and 1st excited state")
                             plt.figtext(0.0,-0.1, "Note: Here the value of \u03B8 runs from 0 to 2\u03C0. Since the angular probability distribution \n of ground state and the 1st excited state are same this plot will be similar for the two states.")
                             plt.show()
                             plt.plot(rad, r,)
                             plt.title("Radial pobability density distribution for ground state")
                             plt.xlim(0,20)
                             plt.xlabel("$r$")
                             plt.ylabel("$|rR_{00}(r)|^{2}$")
                             plt.show()
                        elif (i==2 and a==2 and j==0 and b==0 and k==0 and c==0):
                             plt.polar(angle, s_h,"g.")
                             plt.title("Angular probability density distribution for 1st excited state")
                             plt.figtext(0.0,-0.1, "Note: Here the value of \u03B8 runs from 0 to \u03C0 which are the limits of the integration \n for finding the angular probability distribution.")
                             plt.show()
                             plt.plot(rad, r,)
                             plt.title("Radial pobability density distribution for 1st excited state")
                             plt.xlim(0,20)
                             plt.xlabel("$r$")
                             plt.ylabel("$|rR_{10}(r)|^{2}$")
                             plt.show()
                        print("n=",i,"n_prime=",a,"l=",j,"l_prime=",b,"m=",k,"m_prime=",c,":--")
                        print("----------------------------------------------")
                        print("Value of integration = ",integration)
                        print("\n")

