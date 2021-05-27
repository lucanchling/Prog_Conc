import multiprocessing as mp
from multiprocessing import Process, Value
import time ,sys

def processA(sem1):
    sem1.acquire()
    print ("A")
    time.sleep(1)
    sem1.release()
    sem1.release()
    sem1.release()
    sys.exit(0)
    
def processB(sem1):
    sem1.acquire()
    print ("B")
    time.sleep(1)
    sem2.release()
    sys.exit(0)
    
def processC(sem1):
    sem1.acquire()
    print ("C")
    time.sleep(1)
    sem2.release() 
    sys.exit(0)
    
def processD(sem1):
    sem1.acquire()
    print ("D")
    time.sleep(1)
    sem1.release()
    sys.exit(0)
    
def processE(sem2):
    sem2.acquire()
    print ("E")
    time.sleep(1)
    sem1.release()
    sys.exit(0)
    
def processF(sem1):    
    sem1.acquire()
    print ("F")
    time.sleep(1)
    sem1.release()
    sys.exit(0)
    
    
sem1=mp.Semaphore(1)    
sem2=mp.Semaphore(1) 
mutex=mp.Lock()
pA=mp.Process(target=processA, args=(sem1,))
pB=mp.Process(target=processB, args=(sem1,))
pC=mp.Process(target=processC, args=(sem1,))
pD=mp.Process(target=processD, args=(sem1,))
pE=mp.Process(target=processE, args=(sem2,))
pF=mp.Process(target=processF, args=(sem1,))

pA.start()
pA.join()
pB.start()
pC.start()
pB.join()
pC.join()
pD.start()
pE.start()
pD.join()
pE.join()
pF.start()
pF.join()
sys.exit(0)
