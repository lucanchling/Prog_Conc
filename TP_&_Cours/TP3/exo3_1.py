#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:41:16 2021

@author: vick.foex
"""

import multiprocessing as mp
import os
from random import randint 

def lecture(r):
    listeNb = []
    nb = 0
    while nb != -1:
            
            listeNb.append(nb)
            nb = r.recv()
            
    return(listeNb)

    
def sumListe(liste):
    s = 0
    for el in liste:
        s += el
    return(s)

N = 10

(rnp, wnp) = mp.Pipe()
(rni, wni) = mp.Pipe()

(rsp, wsp) = mp.Pipe()
(rsi, wsi) = mp.Pipe()

if os.fork() != 0: # impaire
    for i in range(N):
        nb = randint(0, 100)
        if nb % 2 == 0:
            wnp.send(nb)
        else:
            wni.send(nb)
    
    wnp.send(-1)
    wni.send(-1)
    
    si = rsi.recv()
    sp = rsp.recv()
    
    print( si + sp )


else :

    if os.fork() != 0: # impaire 
        wsi.send( sumListe ( lecture(rni) ) )
    
    else : # paire
        wsp.send( sumListe( lecture(rnp) ))