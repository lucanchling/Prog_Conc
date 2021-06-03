import sys
mots =sys.argv[1:]



for indice,mot in enumerate(mots):
    inverse=""
    for i in range(len(mot)-1,-1,-1):
        inverse+=mot[i] 
    print(inverse)
