import sys
import os
import time

N = sys.argv[1]
try :
    N=int(N)
except ValueError:
    print("Erreur --> un nombre est attendu comme argument")
    sys.exit(0)


for i in range(N):
    pid_fils = os.fork()
    if pid_fils == 0:    
        print('Mon pid :',os.getpid(),'- Celui de mon PAPA :', os.getppid())
        time.sleep(2*i)
        sys.exit(i)
    else:
        pid_fils, etat = os.wait()
        print("pid : ",pid_fils,"- etat :",os.WEXITSTATUS(etat))


#pid_fils, etat = os.wait()
#print("pid : ",pid_fils,"- etat :",etat)