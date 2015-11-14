import sys
import os
# for example, to delete 3989161.edique02 to 3989167.edique02
# enter : python delete_scal_test_jobs.py 398916 1 7 
head = sys.argv[1]  
start = int(sys.argv[2])
end = int(sys.argv[3])
#print "deleting job from", start ,"to",end
for i in range(start,end+1):
     job = head+str(i)
     print "deleting ", job
     os.system("qdel {}".format(job))
