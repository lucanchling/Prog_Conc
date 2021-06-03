from random import randint
import os

try:
    os.mkfifo("nbPair",0o0644)
except FileExistsError:
    print("Pipe nbPair inexistant")

try:
    os.mkfifo("nbImpair",0o0644)
except FileExistsError:
    print("Pipe nbImpair inexistant")


Pair = os.open("nbPair",os.O_WRONLY)
Impair = os.open("nbImpair",os.O_WRONLY)

for i in range(N):
    j = randint(0,10000)
    # Pair
    if j%2 == 0:
        os.write(Pair,j)
    # Impaire
    else:
        os.write(Impair,j)

os.write(Pair,"-1")
os.write(Impair,"-1")

fdp = os.open("sommePairs",os.O_RDONLY)
fdi = os.open("sommeImpairs",os.O_RDONLY)

sPairs = os.read(fdp)
sImpairs = os.read(fdi)

os.close(fdp)
os.close(fdi)

print("La Somme vaut :",sPairs + sImpairs)