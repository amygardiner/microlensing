#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:27:29 2021

@author: amygardiner
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy.interpolate import make_interp_spline, BSpline
from scipy.optimize import curve_fit

t = np.loadtxt('micro-2.dat', unpack='False', usecols=(0,))
m_t_real = np.loadtxt('micro-2.dat', unpack='False', usecols=(1,))
m_t_err = np.loadtxt('micro-2.dat', unpack='False', usecols=(2,))
"""
t = list(t)
m_t_real =  m_t_real
m_t_real = list(m_t_real)
m_t_err = list(m_t_err)
"""
plt.errorbar(t, m_t_real, yerr=m_t_err, fmt='.', label='Data')
plt.xlabel('Time')
plt.ylabel('M(t)')
plt.title('Plot of Ogle MW data (micro-2)')


def calc_magnitude(t, u_0, t_0, t_E, f_b, m_psf):
    
    p = (u_0)**2
    q = ( (t - t_0) / (t_E) )**2
    
    r = np.sqrt(p + q)
    s = (r**2 + 2) / (r * (np.sqrt(r**2 + 4)))
    
    a = (s * f_b) + (1 - f_b)
    m_t_temp = m_psf - (2.5 * np.log10(a))
    return m_t_temp

times = np.linspace(2452000,2455000,5000)
magnitudes = calc_magnitude(times, 0.0268, 2454550.4236, 20.0081, 0.8581, 18.6248)

popt, pcov = curve_fit(calc_magnitude, t, m_t_real, p0=np.asarray([0.01,2454551,20,0.1,19]), sigma=m_t_err, absolute_sigma=True, maxfev=2000)
#popt, pcov = curve_fit(calc_magnitude, times, magnitudes, p0=np.asarray([0.01,2454551.0,20.0,0.1,19.0]), maxfev=5000, absolute_sigma=True)

plt.axis([2452000, 2455000, 19.5, 16])
plt.plot(t, calc_magnitude(t, *popt),'r',linewidth=2, label='fit: $u_0$=%.4f, $t_0$=%.4f, $t_E$=%.4f, $f_b$=%.4f, $m_{psf}$=%.4f' % tuple(popt))
plt.legend()
plt.show()