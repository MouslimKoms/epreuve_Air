import sys 

def ma_fonction(array_de_strings, separateur):
    # vérification des arguments
    if len(array_de_strings) < 1 or separateur not in [' ', ' \t', ' \n']:
        print("Error : Les arguments ne sont pas valides.")
        sys.ext(1)
     #Transformation du tableau en une seule chaine de caractères   
    chaine = separateur.join(array_de_strings)
    return chaine
#Appel de la fonction avec les arguments du programme
if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Error: Le programme nécessite au moins deux arguments.")
        sys.exit(1)
    separateur = sys.argv[-1]
    array_de_strings = sys.argv[1:-1]
    resultat = ma_fonction(array_de_strings, separateur)
    print(resultat)