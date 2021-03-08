import matplotlib.pyplot as plt
import numpy as np
import matplotlib

m = np.loadtxt('statsnoanomaly.txt', unpack='False', usecols=(1,), delimiter=' ')
s = np.loadtxt('statsnoanomaly.txt', unpack='False', usecols=(3,), delimiter=' ')

x = [6.248557, 10.32208, 5.924572, 5.807755, 5.414352, 5.320295, 6.087314, 5.692202, 12.37823] 

#stats.txt is all 10 images
#statsnoanomaly.txt removes the largest seeing value
#add 71.62689 after 10.32208 if using stats.txt

plt.errorbar(x, m, yerr=s, fmt='.b' )
plt.xlabel('Seeing')
plt.ylabel('Mean')
plt.title('Mean and scatter values for DIA process of each test image')
plt.legend()
plt.show()