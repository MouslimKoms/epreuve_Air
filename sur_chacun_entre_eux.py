import sys
#vérification de la validité des arguments 

if len(sys.argv) < 3 or not sys.argv[-1][0] in ['+','-'] and sys.argv[-1][1:].isdigit():
    print("Error : Le programme nécessite au moins deux entier suivis d'une opération.")
    sys.exit(1)
#Récupération de la liste d'entiers à partir des arguments du programme 
entiers = [int (arg) for arg in sys.argv[1:-1]]
#Récupération de l'opération à appliquer (dernier argument)
operation = int(sys.argv[-1])
#Application de l'opération sur la liste d'entiers
resultats = []
#Vérification de l'opération et application sur la liste d'entiers
for entier in entiers:
    
    if sys.argv[-1][0] == '+':
        resultat = entier + operation
       
    else:
        resultat = entier - operation
    resultats .append(resultat)
    
    print(resultat)


