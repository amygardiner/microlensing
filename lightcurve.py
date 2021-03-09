#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:18:37 2021

@author: amygardiner
Python program to plot light-curves for M31 objects distinguished using DIA techniques with ISIS.
These are then compared with object data directly sourced from the Angstrom survey.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy.interpolate import make_interp_spline, BSpline

"""
x = np.loadtxt('lc529.data', unpack='False', usecols=(0,))
y = np.loadtxt('lc529.data', unpack='False', usecols=(1,))
err = np.loadtxt('lc529.data', unpack='False', usecols=(2,))


x = np.loadtxt('ang_event_i.data', unpack='False', usecols=(0,))
y = np.loadtxt('ang_event_i.data', unpack='False', usecols=(1,))
err = np.loadtxt('ang_event_i.data', unpack='False', usecols=(2,))

"""
x = np.loadtxt('ang_event_iii.data', unpack='False', usecols=(0,))
y = np.loadtxt('ang_event_iii.data', unpack='False', usecols=(1,))
err = np.loadtxt('ang_event_iii.data', unpack='False', usecols=(2,))
"""

x = np.loadtxt('lc1653.data', unpack='False', usecols=(0,))
y = np.loadtxt('lc1653.data', unpack='False', usecols=(1,))
err = np.loadtxt('lc1653.data', unpack='False', usecols=(2,))
"""
y = -1 * y

x = list(x)
y = list(y)
err = list(err)


plt.errorbar(x, y, yerr=err, fmt='.b')
plt.xlabel('Time')
plt.ylabel('Flux')
#plt.title('Light Curve of Object i at $x$ = 401.5, $y$ = 486.8')
#plt.title('Light Curve of Angstrom Event i')
plt.title('Light Curve of Angstrom Event iii')
#plt.title('Light Curve of Object iii at $x$ = 971.6, $y$ = 1052.8')
plt.legend()
plt.show()