import sys
for arg in sys.argv: 
    k=arg
k = int(k)
print "#PBS -q regular"
print "#PBS -l mppwidth=1"
print "#PBS -l walltime=05:00:00"
print "#PBS -N {}cluster".format(k)
print "#PBS -e $PBS_JOBNAME.$PBS_JOBID.err"
print "#PBS -o $PBS_JOBNAME.$PBS_JOBID.out"
print "#PBS -A m2218"
print "export LD_LIBRARY_PATH=/global/homes/d/dorislee/anaconda/lib:$LD_LIBRARY_PATH"
print "cd /project/projectdirs/astro250/doris/halo/halo_find/minibatch_kmeans2"
print "aprun -n 1 /global/homes/d/dorislee/anaconda/bin/python mbk.py {}".format(k)
