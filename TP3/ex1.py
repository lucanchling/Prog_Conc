import multiprocessing as mp
import os, sys

msg = "Salut (de ton papa)"

(dfr,dfw) = mp.Pipe()

pid = os.fork()

if pid != 0:
    dfr.close()
    n = dfw.send(msg)
    print("Le père a transmis le message",n,"c'était le proc n°",os.getppid())
    dfw.close()
else:
    dfw.close()
    msgR = dfr.recv()
    print("le fils a reçu le message",msgR,"c'est le proc n°",os.getpid())
    dfr.close()

sys.exit(0)