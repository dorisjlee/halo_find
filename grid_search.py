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
debug("Loading Particle Data")
ds = yt.load("../ds14_scivis_0128_e4_dt04_1.0000")
ad = ds.all_data()
x = ad[("all","particle_position_x")]
y = ad[("all","particle_position_y")]
z = ad[("all","particle_position_z")]
debug("Creating train test split samples")
train = []
test = []
N = 20#50
N_split = 4#10
for n in np.arange(N):
    if n >N_split:
#         train.append(list(get_halo(filtered_catalog)[-1][n][0])[:6])
        train.append([x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
    elif n<N_split:
#         test.append(list(get_halo(filtered_catalog)[-1][n][0])[:6])
        test.append([x[n].in_cgs(),y[n].in_cgs(),z[n].in_cgs()])
train = np.array(train)
test = np.array(test)
debug("training set size : ", np.shape(train))
debug("testing  set size : ", np.shape(test))

debug("Conducting KMeans on the training set")
num_clusters=3
clf = KMeans(n_clusters=num_clusters)
clf.fit(train)
centers=clf.cluster_centers_
labels=clf.predict(train)

debug("Hyperparameter tuning")
k_range = range(1, len(train)/2)
param_grid = dict(n_clusters=k_range)
grid = GridSearchCV(clf, param_grid, cv=10, scoring='accuracy')
debug(grid)
debug("Conducting hyperparameter grid search")
grid.fit(train, labels)
debug("Writing out grid scores and plotting")
info =[]
scores=[]
for i in grid.grid_scores_:
    info.append([i[0]["n_clusters"], i[1], i[2].std()])
    #so i[2] is the list of results from cross validating 10 times (K folds, K=10)
    scores.append(i[2])
np.savetxt("info.txt",info,header="n_clusters         mean_score      std_score")
np.savetxt("scores.txt",scores)
