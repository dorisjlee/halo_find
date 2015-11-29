import os
os.chdir("/project/projectdirs/astro250/doris/halo/darksky_catalog/")
import yt
yt.funcs.mylog.setLevel(50)
from numpy import float64
from darksky_catalog import darksky
center = np.array([-2505805.31114929,  -3517306.7572399, -1639170.70554688])
width = 50.0e3 # 5 Mpc
bbox = np.array([center-width/2, center+width/2])
ds = darksky['ds14_a']#['halos_a'].load(bounding_box = "None", midx = 7)
print ds.datasets
halo = darksky['ds14_a']['halos_a_1.0000'].load(bounding_box = "None", midx = 7)
filtered_catalog =darksky['ds14_a']['filtered_1e15_a_1.0000']
N=136591 
halo_info=[]
for i in np.arange(N):
    halo_info.append([i for i in filtered_catalog.get_halo(i)])
    print i
np.savetxt("halo_catalog.txt",halo_info) 
