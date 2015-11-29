import numpy as np
import yt
import sklearn
yt.funcs.mylog.setLevel(50)
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.cluster import KMeans
from sklearn.grid_search import GridSearchCV
DEBUG= True
def debug(s,n=""):
    if DEBUG:
        print s , n
debug("Loading Particle Data")
ds = yt.load("../ds14_scivis_0128_e4_dt04_1.0000")
ad = ds.all_data()
x = ad[("all","particle_position_x")]
y = ad[("all","particle_position_y")]
z = ad[("all","particle_position_z")]
debug("Creating train test split samples")
m = ad[("all","mass")]
idx = ad[("all","particle_index")]
train = []
#test = []
N = 2097152
#N_split = 100#100#524288
for n in np.arange(N):
    #if n >N_split:
    train.append([idx[n],m[n].in_cgs(),x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
#         train.append([x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
#    elif n<N_split:
#        test.append([idx[n],m[n].in_cgs(),x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
#         test.append([x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
train = np.array(train)
#test = np.array(test)
# debug("training set size : ", np.shape(train))
# debug("testing  set size : ", np.shape(test))
#np.savetxt("test.txt",test)
np.savetxt("train.txt",train)
# Explicit Grid Search
k_range = np.arange(1,1048576,100) #range(1, 250)
avrg = open('avrg_dens.txt', 'a')
for k in k_range:
    debug("{} clusters test".format(k))
    clf = KMeans(n_clusters=k)
#     debug(np.shape(train[:,2:]))
    clf.fit(train[:,2:])#ignoring idx and mass
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
    #             if np.linalg.norm(train[pcl_idx][2:]-centers[i])!=0:
            for pcl_idx in np.where(labels==i)[0]:
    #                 if i ==27: print "dist: ",np.linalg.norm(train[pcl_idx][2:]-centers[i])
                numerator += np.linalg.norm(train[pcl_idx][2:]-centers[i])
#                 if numerator ==0 : print "identical: ",train[pcl_idx][2:],centers[i],np.where(labels==i)[0]
    #             if i ==27: print "numerator: " , numerator
            if numerator !=0 :
                rad =numerator/N
                volume = (4./3.*np.pi*rad**3)
        #             if rad ==0 : print i , rad
        #             print volume
                mass = 2.75491975e43 * N
                density = mass / volume
            else:#ignore single centroid clusters
#                 print "centers: ",centers[i]
#                 print "train: ",train
                N-=1 #don't count them in the cluster, actually this doesn't matter N is not used anyways 
                #density=0 #should not append the zero densities this brings down the average
            if numerator !=0 :densities.append(density)
        avrg.write(str(np.mean(densities))+"\n")
    np.savetxt("density{}.txt".format(k),densities)
    np.savetxt("centers{}.txt".format(k),centers)
    np.savetxt("labels{}.txt".format(k),labels)
avrg.close()
