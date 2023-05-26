import numpy as np
import matplotlib.pyplot as plt
from VBS_plot import VBS_plot

## Simple test data to see the plot
np.random.seed(17)
g1 =   np.random.rand(50,)
g2 = 2*np.random.rand(75,)+3
n1 = len(g1)
n2 = len(g2)
text_axis  = 'test data'
text_title = 'TEST'
labels     = ['g1','g2']

VBS_plot(g1,g2,n1,n2,text_axis,text_title,labels)
plt.show()