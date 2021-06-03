from os import fork,getpid,getppid

for i in range(3):
    pid = getpid()
    ppid = getppid()
    retour = fork()
    print('i :', i,'- je suis le proc : ',pid,'- mon père est :',ppid, '- retour :',retour)