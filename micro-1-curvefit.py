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

t = np.loadtxt('micro-1.dat', unpack='False', usecols=(0,))
m_t_real = np.loadtxt('micro-1.dat', unpack='False', usecols=(1,))
m_t_err = np.loadtxt('micro-1.dat', unpack='False', usecols=(2,))

plt.errorbar(t, m_t_real, yerr=m_t_err, fmt='.', label='Data')
plt.xlabel('Time')
plt.ylabel('M(t)')
plt.title('Plot of Ogle MW data (micro-1)')


def calc_magnitude(t, u_0, t_0, t_E, f_b, m_psf):
    
    p = (u_0)**2
    q = ( (t - t_0) / (t_E) )**2
    
    
    r = np.sqrt(p + q)
    s = (r**2 + 2) / (r * (np.sqrt(r**2 + 4)))
    #s = r**(-1)
    
    a = (s * f_b) + (1 - f_b)
    m_t_temp = m_psf - (2.5 * np.log10(a))
    return m_t_temp

times = np.linspace(2452000,2455000,5000)
magnitudes = calc_magnitude(times, 0.0633, 2454539.2891, 20.6304, 0.5488, 18.8914)

popt, pcov = curve_fit(calc_magnitude, t, m_t_real, p0=np.asarray([0.06,2454538.0,20.0,0.1,19.0]), maxfev=5000, sigma=m_t_err, absolute_sigma=True)
#popt, pcov = curve_fit(calc_magnitude, times, magnitudes, p0=np.asarray([0.06,2454538.0,20.0,0.1,19.0]), maxfev=5000, absolute_sigma=True)

#errors need to be unity for plotting the linspace

plt.axis([2452000, 2455000, 19.5, 16])
plt.plot(t, calc_magnitude(t, *popt),'r',linewidth=2, label='fit: $u_0$=%.4f, $t_0$=%.4f, $t_E$=%.4f, $f_b$=%.4f, $m_{psf}$=%.4f' % tuple(popt))
plt.legend()
plt.show()