import os
import sys
import time

if os.fork()==0:
    print("Le processus fils = ",(os.getpid()))
    sys.exit(5)

print ("Le processus PERE = %d"%(os.getpid()) )
time.sleep(10)
print ("Sortie après 10 secondes")
pid, status = os.wait()
print ("sortie du wait()")
time.sleep(10)
print ("pid = %d - status = %d"%( pid, os.WEXITSTATUS(status) ) )
sys.exit(0)