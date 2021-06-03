from os import fork, wait, execv

while True:
    lire_commande(commande,para)
    if (fork() != 0):
        wait()
    else:
        execv(commande,para)