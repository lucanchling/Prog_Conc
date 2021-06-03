import sys, os,time,signal

pid = os.fork()

def mess1(signal,frame):
    time.sleep(1)
    print("Message 1")
    time.sleep(1)
def mess2(signal,frame):
    time.sleep(1)
    print("Message 2")
    time.sleep(1)

if pid != 0:
    # Père
    for i in range(150):
        if i == 3 or i==5:
            os.kill(pid,signal.SIGUSR1)
        print("Luke, I'm your Father")
        time.sleep(1)
        if i==9:
            time.sleep(1)
            os.kill(pid,signal.SIGUSR2)
            time.sleep(1)
else:
    #Fils
    while True:
        print("I'm your Son")
        signal.signal(signal.SIGUSR1, mess1)
        signal.signal(signal.SIGUSR2, mess2)