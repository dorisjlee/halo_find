import os
os.chdir("/project/projectdirs/astro250/doris/halo/darksky_catalog/")
print os.getcwd()
import yt
import numpy as np 
yt.funcs.mylog.setLevel(50)
from numpy import float64
from darksky_catalog import darksky
import sys
for arg in sys.argv:
    k=arg
k = int(k) # Batch Number 
N=136592
n=2000#size of each batch
halo_per_batch = N/n #number of haloes in each batch 
start = k*halo_per_batch #starting halo # 
end = start +halo_per_batch +1 #plus 1 because np.arange ending convention  
print "Batch {}: Halo #{} to #{}".format(k,start,end)
ds = darksky['ds14_a']#['halos_a'].load(bounding_box = "None", midx = 7)
halo = darksky['ds14_a']['halos_a_1.0000'].load(bounding_box = "None", midx = 7)
filtered_catalog =darksky['ds14_a']['filtered_1e15_a_1.0000']
halo_info=[]
for i in np.arange(k,ending):
    print i 
    halo_info.append([j for j in filtered_catalog.get_halo(i)])
np.savetxt("haloinfo{}.txt".format(num),halo_info)
