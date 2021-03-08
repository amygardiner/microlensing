import matplotlib.pyplot as plt
import numpy as np
import matplotlib

f = np.loadtxt('seeing_stats.csv', unpack='False', usecols=(2,), delimiter=',')

bins = np.linspace(4, 200, 80) 

plt.hist(f, histtype='bar', bins = bins)
plt.xlabel('Seeing')
plt.ylabel('Number of images')
plt.title('Distribution of Seeing')
plt.legend()
plt.show()