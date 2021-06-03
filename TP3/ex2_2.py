import os

(dfr1,dfw1) = os.pipe()
(dfr2,dfw2) = os.pipe()

fd = os.open("ex1.py",os.O_RDONLY)
fd1 = os.open("sortie",os.O_WRONLY | os.O_CREAT, 0o0644)

sort = os.fork()

if sort != 0:
    os.close(dfr1)
    os.close(dfr2)
    os.close(dfw2)
    os.dup2(fd,0)
    os.dup2(dfw1,1)
    os.close(dfw1)
    os.execlp("sort","sort")
else:
    grep = os.fork()
    if grep != 0:
        os.close(dfr2)
        os.close(dfw1)
        os.dup2(dfr1,0)
        os.dup2(dfw2,1)
        os.close(dfr1)
        os.close(dfw2)
        os.execlp("grep","grep","p")
    else:
        os.close(dfr1)
        os.close(dfw1)
        os.close(dfw2)
        os.dup2(dfr2,0)
        os.dup2(fd1,1)
        os.close(dfr2)
        os.execlp("tail","tail","-n","-5")

os.exit(0)
