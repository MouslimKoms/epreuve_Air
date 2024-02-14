import sys
#Vérification de la validité des arguments 
if len(sys.argv) != 2:
    print("Error: Le programme nécessite un seul argument .")
    sys.exit(1)
#Récupération de la chaine de caractères à partir des arguments du programme
chaine = sys.argv[1]

# Affiche de la chaine en évitant les caractères identiques adjacents 
nouvelle_chaine = " "
for i in range(len(chaine)):
    if i == 0 or chaine[i] != chaine[i-1]:
        nouvelle_chaine += chaine[i]
print(nouvelle_chaine)