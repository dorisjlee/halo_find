# k_range to try 
#10 hr jobs
#declare -a arr=(100000 200000 210000 220000 230000 240000 250000 260000 270000 280000 290000 300000 400000) 
#declare -a arr=(10000 20000 30000 40000 50000 60000 )
declare -a arr=(31000 33000 35000 37000 39000 41000 43000 45000 47000 49000 55000)
for k in "${arr[@]}"
do
   #Call python script that generates output of new run.pbs
   /global/homes/d/dorislee/anaconda/bin/python getscript_cori.py $k > run.pbs
   #/global/homes/d/dorislee/anaconda/bin/python getscript.py $k > run.pbs
   echo "Submitting $k"
   sbatch run.pbs
 #  qsub run.pbs
done
