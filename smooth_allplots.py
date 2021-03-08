#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:26:53 2021

@author: amygardiner
"""

import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

def is_float(number):
    
    try:
        float(number)
        return True

    except:
        return False
    

input_file_1 = open('1.csv','r')

data_1 = np.zeros((0,3))

for line in input_file_1:
    if line[0] != '%':
        split_up = line.split(',')
        if is_float(split_up[0]) and is_float(split_up[1]) and is_float(split_up[2]):
            temp = np.array([float(split_up[0]), float(split_up[1]), float(split_up[2])])
            data_1 = np.vstack((data_1, temp))

x_data_1 = data_1[:,0]
y_data_1 = data_1[:,1]
y_error_1 = data_1[:,2]          

xnew_1 = np.linspace(-5, 5, 300)
spl_1 = make_interp_spline(x_data_1, y_data_1)
y_smooth_1 = spl_1(xnew_1)
plt.plot(xnew_1, y_smooth_1, label='$u_0$ = 1')
plt.errorbar(x_data_1, y_data_1, yerr=y_error_1, fmt='.b' )


input_file_2 = open('0_3.csv','r')

data_2 = np.zeros((0,3))

for line in input_file_2:
    if line[0] != '%':
        split_up = line.split(',')
        if is_float(split_up[0]) and is_float(split_up[1]) and is_float(split_up[2]):
            temp = np.array([float(split_up[0]), float(split_up[1]), float(split_up[2])])
            data_2 = np.vstack((data_2, temp))

x_data_2 = data_2[:,0]
y_data_2 = data_2[:,1]
y_error_2 = data_2[:,2]          

xnew_2 = np.linspace(-5, 5, 300)
spl_2 = make_interp_spline(x_data_2, y_data_2, k=2)
y_smooth_2 = spl_2(xnew_2)
plt.plot(xnew_2, y_smooth_2, label='$u_0$ = 0.3')
plt.errorbar(x_data_2, y_data_2, yerr=y_error_2, fmt='.', color='red' )

input_file_3 = open('0_1.csv','r')

data_3 = np.zeros((0,3))

for line in input_file_3:
    if line[0] != '%':
        split_up = line.split(',')
        if is_float(split_up[0]) and is_float(split_up[1]) and is_float(split_up[2]):
            temp = np.array([float(split_up[0]), float(split_up[1]), float(split_up[2])])
            data_3 = np.vstack((data_3, temp))

x_data_3 = data_3[:,0]
y_data_3 = data_3[:,1]
y_error_3 = data_3[:,2]          

xnew_3 = np.linspace(-5, 5, 300)
spl_3 = make_interp_spline(x_data_3, y_data_3, k=2)
y_smooth_3 = spl_3(xnew_3)
plt.plot(xnew_3, y_smooth_3, label='$u_0$ = 0.1')
plt.errorbar(x_data_3, y_data_3, yerr=y_error_3, fmt='.', color='green' )

input_file_4 = open('0_03.csv','r')

data_4 = np.zeros((0,3))

for line in input_file_4:
    if line[0] != '%':
        split_up = line.split(',')
        if is_float(split_up[0]) and is_float(split_up[1]) and is_float(split_up[2]):
            temp = np.array([float(split_up[0]), float(split_up[1]), float(split_up[2])])
            data_4 = np.vstack((data_4, temp))

x_data_4 = data_4[:,0]
y_data_4 = data_4[:,1]
y_error_4 = data_4[:,2]          

xnew_4 = np.linspace(-5, 5, 300)
spl_4 = make_interp_spline(x_data_4, y_data_4, k=2)
y_smooth_4 = spl_4(xnew_4)
plt.plot(xnew_4, y_smooth_4, label='$u_0$ = 0.03')
plt.errorbar(x_data_4, y_data_4, yerr=y_error_4, fmt='.', color="black" )

plt.legend(loc='best')
plt.xlabel("Distance ($t$/$t_E$)")
plt.ylabel("Magnification $A$")
plt.show()