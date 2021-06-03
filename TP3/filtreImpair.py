import os

try:
    os.mkfifo("SommeImpairs",0o0644)
except FileExistsError:
    print("Pipe SommeImpair inexistant")


Impair = os.open("nbImpair",os.O_RDONLY)

somme = 0

while int(Impair) != -1:
    somme += 1

fdi = os.open("SommeImpairs",os.O_WRONLY)

os.write(fdi,somme)

os.close(fdi)