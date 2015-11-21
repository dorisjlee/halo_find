# k_range to try 
# 20 hr job 
#declare -a arr=(50000 60000  70000 80000 100000) 
#10 hr jobs
declare -a arr=(27000 28000 33000 45000  50000 )
for k in "${arr[@]}"
do
   #Call python script that generates output of new run.pbs
   /global/homes/d/dorislee/anaconda/bin/python getscript.py $k > run.pbs
   echo "Submitting $k"
   qsub run.pbs
done
