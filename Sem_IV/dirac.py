#  Q9b  Dirac delta function
import math as cm

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as intg

sig = float(input("Initial value of Sigma = "))

# x1 = lambda x: (x+3) * cm.exp(-((x-2)**2)/(2*sig**2)) /(cm.sqrt(2*np.pi) * sig)
# x2 = lambda x: (x+3)**2 * \
#     cm.exp(-((x-2)**2)/(2*sig**2)) /(cm.sqrt(2*np.pi) * sig)
# x3 = lambda x: np.sin(x+3) * \
#     cm.exp(-((x-2)**2)/(2*sig**2)) /(cm.sqrt(2*np.pi) * sig)
# x4 = lambda x: np.cos(x+3) * \
#     cm.exp(-((x-2)**2)/(2*sig**2)) /(cm.sqrt(2*np.pi) * sig)
# x5 = lambda x: cm.exp(x+3) * \
#     cm.exp(-((x-2)**2)/(2*sig**2)) /(cm.sqrt(2*np.pi) * sig)
x6 = (
    lambda x: cm.log(x + 3)
    * cm.exp(-((x - 2) ** 2) / (2 * sig**2))
    / (cm.sqrt(2 * np.pi) * sig)
)

a = []
sigma = []
for i in range(3):
    ai, err = intg.quad(x6, 2 - 5 * sig, 2 + 5 * sig)
    a.append(ai)

    sigma.append(sig)
    sig = sig / 10.0
a = np.array(a)
sigma = np.array(sigma)

print("Used function is f(x) = log(x).")
print("As the value of Sigma reaches to ", sigma[-1])
print(
    "The value of integration reaches to ", a[-1], ", i.e, towards f(5) = ", cm.log(5)
)

plt.plot(sigma, a)
plt.title(r"Value of integration for $f(x)=log(x)$ as a function of $\sigma$")
plt.xlabel(r"$\sigma$")
plt.ylabel("Value of integration")
plt.show()

# ------------------------------------------------------
#                        INPUT
# ------------------------------------------------------
# Initial value of Sigma = 1
# ------------------------------------------------------
#                       OUTPUT
# ------------------------------------------------------
# Used function is f(x) = log(x).
# As the value of Sigma reaches to  0.01
# The value of integration reaches to  1.60943498976 ,
# i.e, towards f(5) =  1.6094379124341003
# -------------------------------------------------------
