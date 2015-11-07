import time
import numpy as np
import yt
import sklearn
yt.funcs.mylog.setLevel(50)
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.cluster import KMeans
from sklearn.grid_search import GridSearchCV
#DEBUG= True
#def debug(s,n=""):
#    if DEBUG:
#        print s , n
#debug("Loading Particle Data")
print "Loading Particle Data"
ds = yt.load("../ds14_scivis_0128_e4_dt04_1.0000")
ad = ds.all_data()
x = ad[("all","particle_position_x")]
y = ad[("all","particle_position_y")]
z = ad[("all","particle_position_z")]
#debug("Creating train test split samples")
print "Creating train test split samples"
#m = ad[("all","mass")]
idx = ad[("all","particle_index")]
N = 2097152
#train = np.array([idx[N:],x[N:],y[N:],z[N:]]).T
train = np.array([idx,x,y,z]).T
np.savetxt("train.txt",train)
# Explicit Grid Search
k_range = np.arange(2000, 21000,1000) 
avrg = open('avrg_dens.txt', 'a')
timef = open('time.txt','a')
for k in k_range:
    start = time.time()
    #debug("{} clusters test".format(k))
    print "{} clusters test".format(k)
    clf = KMeans(n_clusters=k,n_jobs=-2)#n_jobs = -2, all CPUs -1 used
    clf.fit(train[:,1:])#ignoring idx and mass
    centers=clf.cluster_centers_
    labels = clf.labels_
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
