import multiprocessing as mp

import os, sys

msg = "monMessage"

(dfr,dfw) = mp.Pipe()
n=dfw.send(msg)
msgRecu = dfr.recv()
dfr.close();dfw.close()
sys.exit(0)
