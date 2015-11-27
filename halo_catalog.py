import os
os.chdir("/project/projectdirs/astro250/doris/halo/darksky_catalog/")
import yt
import numpy as np 
yt.funcs.mylog.setLevel(50)
from numpy import float64
from darksky_catalog import darksky
center = np.array([-2505805.31114929,  -3517306.7572399, -1639170.70554688])
width = 50.0e3 # 5 Mpc
bbox = np.array([center-width/2, center+width/2])
ds = darksky['ds14_a']#['halos_a'].load(bounding_box = "None", midx = 7)
halo = darksky['ds14_a']['halos_a_1.0000'].load(bounding_box = "None", midx = 7)
filtered_catalog =darksky['ds14_a']['filtered_1e15_a_1.0000']
N=136592 
halo_info=[]
for i in np.arange(N):
    print i 
    halo_info.append([j for j in filtered_catalog.get_halo(i)])
np.savetxt("haloinfo.txt",halo_info) 
