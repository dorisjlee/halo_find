## now loop through the above array
declare -a arr=(1 24 48 72 96 120 144 168 ) 
for nproc in "${arr[@]}"
do
   dir="4test$nproc"
   mkdir $dir
   cd $dir
   cp ../parallel_gs_dens_test.py .
   #Call python script that generates output of new run.pbs
   /global/homes/d/dorislee/anaconda/bin/python ../getscript.py $nproc > run.pbs
   echo "Submitting $nproc"
   qsub run.pbs
   cd .. 
done
