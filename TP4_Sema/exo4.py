# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:31:50 2019

@author: noemie.rolland
"""

import multiprocessing as mp
from multiprocessing import Process, Value
import time ,sys
from random import randint

def processusP1():
    for i in range (10) :
        nb1=randint(1,10)
        Q1.put(nb1)
        time.sleep(1)
    
def processusP2():
    for i in range (10) :
        nb2=randint(1,10)
        Q2.put(nb2)
        time.sleep(1)
    
def processusC1(sem1):
    while True :
        sem1.acquire()
        print(Q1.get())
        time.sleep(1)
        sem2.release()
    
def processusC2(sem2):
    while True :
        sem2.acquire()
        print(Q2.get())
        time.sleep(1)
        sem1.release()      
    
    
sem1=mp.Semaphore(1)  
sem2=mp.Semaphore(0) 
Q1=mp.Queue()
Q2=mp.Queue()    
P1=mp.Process(target=processusP1, args=())
P2=mp.Process(target=processusP2, args=())
C1=mp.Process(target=processusC1, args=(sem1,))
C2=mp.Process(target=processusC2, args=(sem2,))


P1.start()
P2.start()
P1.join()
P2.join()

C1.start()
C2.start()
C1.join()
C2.join()
