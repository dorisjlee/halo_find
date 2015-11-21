from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
import numpy as np
import yt
import sklearn
prefix = "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/"
ds = yt.load(prefix+"ds14_scivis_0128_e4_dt04_1.0000")
ad = ds.all_data()
yt.funcs.mylog.setLevel(50) #coerce output null
x = ad[("all","particle_position_x")]
y = ad[("all","particle_position_y")]
z = ad[("all","particle_position_z")]
X= np.array([x,y,z])
X = X.T
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=np.shape(X)[0])
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
centers = ms.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
fig = plt.figure()
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(111, projection='3d')
color = ["red","green","blue","cyan","purple","orange","magenta","brown","yellow","lime"]
for i in range(n_clusters_):
    group  = np.where(labels==i)
    ax.scatter(X[group,0], X[group,1],X[group,2],c=color[i])#, c=c, marker=m)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.savefig("meanshift.png")
