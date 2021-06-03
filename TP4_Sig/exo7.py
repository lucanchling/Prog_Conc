import os, signal, sys, time

pid = os.fork()

if pid == 0:
    while True:
        nb = input("SVP un entier : ")

        try :
            nb = int(nb)
            os.kill(os.getppid(), signal.SIGINT)
            print("OK !")
            sys.exit()

        except :
            pass
else :
    try:
        time.sleep(10)
        print("Toooo Late !")
        os.kill(pid, signal.SIGINT)
    except:
        pass