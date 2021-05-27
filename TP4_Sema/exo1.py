import random
import multiprocessing as mp
from multiprocessing import Process, Value

def processusP1(sem,mutex,somme) :
    i=1
    sommeImpairs=0
    while i < N :
        sommeImpairs=sommeImpairs +L[i]
        i=i+2
    mutex.acquire()
    somme.value+=sommeImpairs
    mutex.release()
    
def processusP2(sem,mutex,somme) :
    j=0   
    sommePairs=0
    while j < N :
        sommePairs=sommePairs +L[j]
        j=j+2
    mutex.acquire() 
    somme.value+=sommePairs
    mutex.release()


N = 15
L=[int(100*random.random()) for i in range(N)]
print(L)
    
sem=mp.Semaphore(0)
somme=mp.Value('i',0)
mutex=mp.Lock() 
process1=mp.Process(target=processusP1, args=(sem,mutex,somme))
process2=mp.Process(target=processusP2, args=(sem,mutex,somme))
process1.start()
process2.start()
process1.join()
process2.join()

print(somme.value)