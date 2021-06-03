import multiprocessing as mp
from multiprocessing import Process, Value
import time ,sys

# EXERCICE 5 
# Exemple 2 Process

# def processusP1(sem1):
#        sem1.acquire()
#        print("Je suis P1")
#        time.sleep(1)
#        sem2.release()
#        sem1.acquire()
#        rdv1()
   
# def processusP2(sem2):
#        sem2.acquire()
#        print("Je suis P2")
#        time.sleep(1)
#        sem1.release()
#        sem1.release()
#        sem1.acquire()
#        rdv2()
#        
#def rdv1():
#    print("rdv1")
#    
#def rdv2():
#    print("rdv2")
#        
#sem1=mp.Semaphore(1)  
#sem2=mp.Semaphore(0) 
#P1=mp.Process(target=processusP1, args=(sem1,))
#P2=mp.Process(target=processusP2, args=(sem2,))
#
#P1.start()
#P2.start()
#P1.join()
#P2.join()

#Exemple 3 Process

def processusP1(sem1):

        print("Je suis P1")
        time.sleep(3)
        sem1.release() #lache un jeton pour P2
        sem1.release() #lache un jeton pour P3
        sem2.acquire() #vérifie que P2 s'est déroulé
        sem3.acquire() #vérifie que P3 s'est déroulé
        rdv1()
    
def processusP2(sem2):

        print("Je suis P2")
        time.sleep(2)
        sem2.release() #lache un jeton pour P1
        sem2.release() #lache un jeton pour P3
        sem1.acquire() #vérifie que P1 s'est déroulé
        sem3.acquire() #vérifie que P3 s'est déroulé
        rdv2()
        
def processusP3(sem3):

        print("Je suis P3")
        time.sleep(1)
        sem3.release() #lache un jeton pour P1
        sem3.release() #lache un jeton pour P2
        sem1.acquire() #vérifie que P3 s'est déroulé
        sem2.acquire() #vérifie que P2 s'est déroulé
        rdv3()
        
def rdv1():
    print("rdv1")
    
def rdv2():
    print("rdv2")
    
def rdv3():
    print("rdv3")
        
sem1=mp.Semaphore(0)  #semaphore contenant les jetons créés par P1
sem2=mp.Semaphore(0) #semaphore contenant les jetons créés par P2
sem3=mp.Semaphore(0) #semaphore contenant les jetons créés par P3
P1=mp.Process(target=processusP1, args=(sem1,))
P2=mp.Process(target=processusP2, args=(sem2,))
P3=mp.Process(target=processusP3, args=(sem3,))

P1.start()
P2.start()
P3.start()
P1.join()
P2.join()
P3.join()

