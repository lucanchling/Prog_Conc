import signal, sys,time

def arretProg(signal,frame):
    print("It's Over")
    sys.exit(0)



while True:
    print("Je travaille")
    time.sleep(1)

