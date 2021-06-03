import sys
notes = sys.argv[1:]

def note(notes):
    moy=0
    if len(notes)<1:
        return "Aucune moyenne à calculer" 
 
    for i,valeur in enumerate(notes):
        try:
            int(valeur)
        except ValueError:
            print("note non valide")
            sys.exit(1)  
        if int(valeur) <0 or int(valeur)>20:
            print("La note",i+1,"est non valide")
            return
            
        else:
            moy+=int(valeur)
    moy=moy/len(notes)

    print("la moyenne est de",round(moy,2))

note(notes)
  