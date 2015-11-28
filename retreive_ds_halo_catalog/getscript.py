import sys
for arg in sys.argv: 
    k=arg
k = int(k)
print "#PBS -q serial"
#print "#PBS -l mppwidth=1"
print "#PBS -l walltime=05:00:00"
print "#PBS -N run{}".format(k)
print "#PBS -l vmem=20GB"
print "#PBS -e $PBS_JOBNAME.$PBS_JOBID.err"
print "#PBS -o $PBS_JOBNAME.$PBS_JOBID.out"
print "#PBS -A m2218"
print "export LD_LIBRARY_PATH=/global/homes/d/dorislee/anaconda/lib:$LD_LIBRARY_PATH"
print "cd /project/projectdirs/astro250/doris/halo/darksky_catalog"
print "aprun -n 1 /global/homes/d/dorislee/anaconda/bin/python halo_catalog.py  {}".format(k)

