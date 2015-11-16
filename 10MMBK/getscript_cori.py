import sys
for arg in sys.argv: 
    k=arg
k = int(k)
print "#!/bin/bash -l"
print "#SBATCH -p regular"
print "#SBATCH -N 1"
print "#SBATCH -o %j.out"
print "#SBATCH -e %j.err"
print "#SBATCH -t 00:05:00"
print "#SBATCH -J {}cluster".format(k)
print "export LD_LIBRARY_PATH=/global/homes/d/dorislee/anaconda/lib:$LD_LIBRARY_PATH"
print "cd /project/projectdirs/astro250/doris/halo/halo_find/10MMBK" 
print "srun -n 1 --unbuffered /global/homes/d/dorislee/anaconda/bin/python mbk.py {}".format(k)
