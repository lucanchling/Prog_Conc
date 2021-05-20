import multiprocessing as mp
import os, sys

(dfr,dfw) = mp.Pipe()

first = os.fork()
if first == 0:
    os.execlp("python3","python3","generateurNombre.py","50")
else:
    second = os.fork()
    if second == 0:
        os.execlp("python3","python3","filtrePair.py")
    else:
        os.execlp("python3","python3","filtreImpair.py")

dfw.send(msg)
msgR = dfr.recv()

sys.exit(0)