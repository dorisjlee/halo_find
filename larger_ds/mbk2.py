import time
import numpy as np
import yt
import sklearn
from sklearn.cluster import MiniBatchKMeans
import sys
for arg in sys.argv:
    k=arg
k = int(k)
yt.funcs.mylog.setLevel(50) #coerce output null
print "{} clusters test".format(k)
num =100000000
print "Loading {} Particles".format(num)
from yt.utilities.sdf import load_sdf
path = 'http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000'
data = load_sdf(path)
x = data['x'][:num]
print x.nbytes
y = data['y'][:num]
z = data['z'][:num]
idx = data['ident'][:num]
#ds = yt.load("../../ds14_scivis_0128_e4_dt04_1.0000")
#ad = ds.all_data()
#x = ad[("all","particle_position_x")]
#y = ad[("all","particle_position_y")]
#z = ad[("all","particle_position_z")]
#idx = ad[("all","particle_index")]
train = np.array([idx,x,y,z]).T
np.savetxt("train.txt",train)
avrg = open('avrg_dens.txt', 'a')
timef = open('time.txt','a')
start = time.time()
print "Conducting MBKMeans"
clf = MiniBatchKMeans(init='k-means++', n_clusters=k, compute_labels=False)
clf.fit(train[:,1:])
labels = clf.predict(train[:,1:])
centers=clf.cluster_centers_
#Density calculation for each cluster
densities =[]
if k ==1:
    density =0 #undefined density for point mass 
    avrg.write(str(density)+"\n")
else:
    for i in np.arange(k):
        numerator = 0
        n_tot = 0
        N=len(np.where(labels==i)[0])
        for pcl_idx in np.where(labels==i)[0]:
            numerator += np.linalg.norm(train[pcl_idx][1:]-centers[i])
        if numerator !=0 :
            rad =numerator/N
            volume = (4./3.*np.pi*rad**3)
            mass = 2.75491975e43 * N
            density = mass / volume
            densities.append(density)
    avrg.write(str(np.mean(densities))+"\n")
np.savetxt("density{}.txt".format(k),densities)
np.savetxt("centers{}.txt".format(k),centers)
np.savetxt("labels{}.txt".format(k),labels)
end = time.time()
timef.write(str(k)+"		"+ str(end-start)+"\n")
print "Time: " , end-start
avrg.close()
