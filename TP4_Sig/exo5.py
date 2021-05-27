import sys, os,time,signal

pid = os.fork()

def steal(signal,frame):
    print("Le fiston a intercepté ton méssage papa")

if pid != 0:
    # Père
    for i in range(150):
        if i == 3:
            os.kill(pid,signal.SIGKILL)
        print("Luke, I'm your Father")
        time.sleep(1)

else:
    #Fils
    while True:
        print("I'm your Son")
        signal.signal(signal.SIGINT, steal)
