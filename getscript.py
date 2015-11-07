import sys
for arg in sys.argv: 
    nproc=arg
nproc = int(nproc)
print "#PBS -q regular"
if nproc<24:
    print "#PBS -l mppwidth=24"
else:
    print "#PBS -l mppwidth={}".format((nproc/24)*24)
print "#PBS -l walltime=03:00:00"
print "#PBS -N {}_test".format(nproc)
print "#PBS -e sctest.$PBS_JOBID.err"
print "#PBS -o sctest.$PBS_JOBID.out"
print "#PBS -A m2218"
print "cd /project/projectdirs/astro250/doris/halo/halo_find/test{}".format(nproc)
print "aprun -n 1 /global/homes/d/dorislee/anaconda/bin/python parallel_gs_dens_test.py" 
