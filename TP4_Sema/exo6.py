import multiprocessing as mp
from multiprocessing import Process, Value
import time ,sys

def emetteur(semR,semE):
    mutex.acquire() #on protege pour qu'un seul emetteur accede aux 2 jetons recpteur
    print ("E franchi mutex")
    semR.acquire() # verif presence de deux recepteurs
    semR.acquire()  # verif presence de deux recepteurs
    print("E débloqué")
    semE.release() #creation jeton pour un recepteur
    semE.release() #creation jeton pour un recepteur
    mutex.release() #on reouvre le verrou
    
def recepteur(semR,semE):
    semR.release() #chaque recepteur créer un jeton 
    print("R la")
    semE.acquire() #chaque recepteur recupere un jeton emetteur
    print("R débloqué")
    
    



   
 
semE=mp.Semaphore(0)  #semaphore dans lequel l'emetteur met ses jetons
semR=mp.Semaphore(0) #semaphore dans lequel le recepteur met ses jetons
mutex=mp.Lock()
lp=[]
for arg in sys.argv :
    if arg=="R":
        R=mp.Process(target=recepteur, args=(semR,semE,))
        lp.append(R)
        R.start()
    if arg=="E":
        E=mp.Process(target=emetteur, args=(semR,semE,))
        lp.append(E)
        E.start()
        
for p in lp :
    p.join()