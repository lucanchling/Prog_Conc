from os import fork,execlp,wait

# Parallèle :
'''
who=fork()
if who == 0:
    execlp('who','who')
else:
    ls = fork()
    if ls == 0:
        execlp('ls','ls','-l')
    else:
        execlp('ps','ps')
'''
# Séquentiel :

who=fork()
if who == 0:
    execlp('who','who')
wait()
ps = fork()
if ps == 0:
    execlp('ps','ps')
wait()
ls = fork()
if ls == 0:
    execlp('ls','ls','-l')
wait()
