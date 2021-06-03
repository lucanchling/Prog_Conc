import sys
mot = sys.argv[1]
inverse =""
for i in range(len(mot)-1,-1,-1):
    inverse+=mot[i]

print(inverse)