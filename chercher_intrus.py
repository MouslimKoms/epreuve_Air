import sys 

#vérification de la validités des arguments

if len(sys.argv) < 2:
    print("Error : Le programe nécessite au moins un argument. ")
    sys.exit(1)
#récupération de la liste à partir des arguments du programme
liste = sys.argv[1:]
#recherche de la valeur qui n'a pas de paire dans la liste 
valeur_sans_paire = None
for element in liste:
    if liste.count(element) %2 == 1:
        valeur_sans_paire = element
        break
#Affichage du résultat
if valeur_sans_paire:
    print(f"Lavaleur sans paire dans la liste est : {valeur_sans_paire}")
else:
    print("Aucune valeur sans paire n'a été trouvée dans la liste.")
    