import yt
yt.funcs.mylog.setLevel(50)
import yt
import numpy as np
from numpy import float64
from darksky_catalog import darksky
filtered_catalog =darksky['ds14_a']['filtered_1e15_a_1.0000']
filtered_catalog.get_halo(136591)
masses=[]
for i in np.arange(136591):
    masses.append(filtered_catalog.get_halo(i)[6])
    #print i
    if i%10000==0:
	print i
	np.savetxt("mass{}.txt".format(i),masses)
np.savetxt("mass.txt".format(i),masses)
