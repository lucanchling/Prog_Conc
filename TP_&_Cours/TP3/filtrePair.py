import os

try:
    os.mkfifo("SommePairs",0o0644)
except FileExistsError:
    print("Somme Pair inexistant")

Pair = os.open("nbPair",os.O_RDONLY)

somme = 0

while int(Pair) != -1:
    somme += 1

fdp = os.open("SommePairs",os.O_WRONLY)

os.write(fdp,somme)

os.close(fdi)