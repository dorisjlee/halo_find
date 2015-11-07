## now loop through the above array
declare -a arr=(1 24 48 72 96 120) 
for nproc in "${arr[@]}"
do
   dir="test$nproc"
   mkdir $dir
   cd $dir
   cp ../parallel_gs_dens_test.py .
   #Call python script that generates output of new run.pbs
   echo $nproc
   /global/homes/d/dorislee/anaconda/bin/python ../getscript.py $nproc > run.pbs
   echo "Submitting $nproc"
   qsub run.pbs
   cd .. 
done
