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
        print s
        print n
def compute_rcm(n_cluster,centroids):
    #since all the particles have the same mass, the center of mass is  just the arithmetic average weighted by the number of particles in each cluster 
    numerator = 0
    n_tot = 0
    for i in np.arange(n_cluster):
        N = len(np.where(labels==i)[0]) #number of particles in each cluster
#         print "n_clusters:", i 
#         print "nuumber of particles in each cluster ", N
#         print "cluster center" , centroids[i]    
        numerator += centroids[i]*N 
#         print "numerator: " , numerator
        n_tot+=N
    rcm = numerator/n_tot
    return rcm
def compute_avrg_rad(n_cluster,centroids):
    numerator = 0
    n_tot = 0
    for i in np.arange(n_cluster):
        numerator += np.linalg.norm(centroids[i]-compute_rcm(n_cluster,centroids))
    return numerator/n_cluster
def verify_cm_calculation(n_cluster,centroids):
    fig  = plt.figure()
    plt.title("xy projection for n_cluster = ".format(n_cluster),fontsize=15)
    plt.plot(centers[:,0], centers[:,1],'o')
    rcm = compute_rcm(n_cluster,centroids)
    plt.plot(rcm[0],rcm[1],"x", color = "red", markersize=13)
    rad = compute_avrg_rad(n_cluster,centroids)
    circle1 = plt.Circle((rcm[0],rcm[1]),rad,color='g',fill=False)
    fig.gca().add_artist(circle1)
    plt.xlabel("X",fontsize=13)
    plt.ylabel("Y",fontsize=13)
    axes().set_aspect('equal', 'datalim')
    plt.savefig("check{}.png".format(n_cluster))
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
test = []
N = 500
N_split = 100
for n in np.arange(N):
    if n >N_split:
        train.append([idx[n],m[n].in_cgs(),x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
#         train.append([x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
    elif n<N_split:
        test.append([idx[n],m[n].in_cgs(),x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
#         test.append([x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
train = np.array(train)
test = np.array(test)
debug("training set size : ", np.shape(train))
debug("testing  set size : ", np.shape(test))
# Explicit Grid Search 
k_range = range(1, 100)
# k_scores = []
densities =[]
densf = open('densities.txt', 'a')
for k in k_range:
    clf = KMeans(n_clusters=k)
    clf.fit(train[:,2:])#ignoring idx and mass 
    centers=clf.cluster_centers_
    labels = clf.labels_
    rad = compute_avrg_rad(k,centers)
    volume = (4./3.*pi*rad**3)
    mass = 2.75491975e43 * len(labels)
    density = mass / volume
#     print density
    verify_cm_calculation(k,centers)
    densities.append(density)
    np.savetxt("centers{}.txt".format(k),centers)
    np.savetxt("labels{}.txt".format(k),centers)
#     print k,"clusters"
#     print centers
#     print labels
    densf.write(density)
