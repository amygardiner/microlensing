#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:37:02 2021

@author: amygardiner
program to perform degenerate difference flux fit for Angstrom M31 light curves.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy.interpolate import make_interp_spline, BSpline
from scipy.optimize import curve_fit

t = np.loadtxt('lc1653.data', unpack='False', usecols=(0,))
f_t = np.loadtxt('lc1653.data', unpack='False', usecols=(1,))
f_t_err = np.loadtxt('lc1653.data', unpack='False', usecols=(2,))


f_t_err = 2*f_t_err #as mentioned in the lab script

t = list(t)
f_t = list(f_t)
f_t_err = list(f_t_err)


def degenerate_flux(t, f_base, t_half, t_0, delta_f_0):
    
    return f_base + (delta_f_0)/np.sqrt(1+ 12*((t-t_0)/t_half)**2)

popt, pcov = curve_fit(degenerate_flux, t, f_t, p0=np.asarray([12000,25,54317,43310]), sigma=f_t_err, absolute_sigma=True, maxfev=2000)

plt.errorbar(t, f_t, yerr=f_t_err, fmt='.b')
plt.plot(t, degenerate_flux(t, *popt),'r',linewidth=3, label='fit: $F_{base}$=%.4f, $t_{1/2}$=%.4f, $t_0$=%.4f, $\Delta f_0$=%.4f' % tuple(popt))
plt.xlabel('Time')
plt.ylabel('Flux')
plt.title('Light Curve with Degenerate Difference Flux Fit of Object at $x$ = 971.6, $y$ = 1052.8')
plt.legend()
plt.show()