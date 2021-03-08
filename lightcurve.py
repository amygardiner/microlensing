import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy.interpolate import make_interp_spline, BSpline


x = np.loadtxt('lc529.data', unpack='False', usecols=(0,))
y = np.loadtxt('lc529.data', unpack='False', usecols=(1,))
err = np.loadtxt('lc529.data', unpack='False', usecols=(2,))

"""
x = np.loadtxt('ang_event_i.data', unpack='False', usecols=(0,))
y = np.loadtxt('ang_event_i.data', unpack='False', usecols=(1,))
err = np.loadtxt('ang_event_i.data', unpack='False', usecols=(2,))
"""
y = -1 * y

x = list(x)
y = list(y)
err = list(err)


plt.errorbar(x, y, yerr=err, fmt='.b')
plt.xlabel('Time')
plt.ylabel('Flux')
plt.title('Light Curve of Object at $x$ = 401.5, $y$ = 486.8')
#plt.title('Light Curve of Angstrom Event i')
plt.legend()
plt.show()