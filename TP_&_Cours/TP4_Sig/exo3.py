import signal, sys,time
fin = False

def arretProg(signal,frame):
    fin = True
    print("It's Over")
    sys.exit(0)

signal.signal(signal.SIGINT,arretProg)

while fin == False:
    print("Je travaille")
    time.sleep(1)

