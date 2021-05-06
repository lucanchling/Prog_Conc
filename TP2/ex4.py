import os
import sys
n=0
for i in range(1,5):
    fils_pid = os.fork()  #1
    if fils_pid > 0 :  #2   --> dans le proc père - valeur nulle --> fils
        os.wait()   #3
        n = i*2
        break
print('n = ',n) #4
sys.exit(0)

# C'est déterministe car wait
# Ce n'est pas un algo déterministe (il dépend de la fermeture des proc - commande wait)
# déterministe : 0,8,6,4,2
# non déterministe : 2,8,0,6,4

# oui si il y a saturation