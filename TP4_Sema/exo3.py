# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:12:57 2019

@author: noemie.rolland
"""

import multiprocessing as mp
from multiprocessing import Process
import time ,sys

def processus1(sem1):
    #...
    print ("T1")
    time.sleep(1)
    sem1.release()
    sys.exit(0)
    
def processus2(sem1):
    print("Je suis le 2")
    sem1.acquire()
    print ("T2")
    time.sleep(1)
    sem1.release()
    sys.exit(0)   
    
    
sem1=mp.Semaphore(0)    

p1=mp.Process(target=processus1, args=(sem1,))
p2=mp.Process(target=processus2, args=(sem1,))

p1.start()
p2.start()


p1.join()
p2.join()