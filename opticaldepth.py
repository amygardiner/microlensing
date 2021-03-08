#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:49:17 2021

@author: amygardiner
"""

from scipy.integrate import quad
import numpy as np

"""
#Galactic Bulge
R_0 = 8000 #parsecs
a = 5000 #parsecs
rho_0 = 0.01 * (1.989 * 10**(30)) #kg parsecs^-3
D_s = 8000 #parsecs
c = 9.7156 * (10**-9) #parsecs^-1
G = 2.261 * (10**-60) #parsec^3 kg^-1 s^-2
l = np.deg2rad(1)


#Large Magellanic Cloud
R_0 = 8000 #parsecs
a = 5000 #parsecs
rho_0 = 0.01 * (1.989 * 10**(30)) #kg parsecs^-3
D_s = 50000 #parsecs
c = 9.7156 * (10**-9) #parsecs^-1
G = 2.261 * (10**-60) #parsec^3 kg^-1 s^-2
l = np.deg2rad(280)
"""

#Small Magellanic Cloud
R_0 = 8000 #parsecs
a = 5000 #parsecs
rho_0 = 0.01 * (1.989 * 10**(30)) #kg parsecs^-3
D_s = 60000 #parsecs
c = 9.7156 * (10**-9) #parsecs^-1
G = 2.261 * (10**-60) #parsec^3 kg^-1 s^-2
l = np.deg2rad(303)



def integrand(D_l, G, rho_0, D_s, a, R_0, c):
    
    temp1 = 4 * np.pi * (D_l)**2 * G * (rho_0)
    temp2 = (D_s - D_l) * (a**2 + R_0**2)
    temp3 = c**2 * D_s * D_l 
    temp4 = a**2 * (D_l)**2 * R_0**2 - (2 * (R_0**2) * (np.cos(l))**2 ) 
    
    return (temp1 * temp2) / (temp3 * temp4)

I = quad(integrand, 0, D_s, args=(G, rho_0, D_s, a, R_0, c))
#I here is optical depth tau / f

print(I)

