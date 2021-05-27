import sys, os,time,signal

pid = os.fork()

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
