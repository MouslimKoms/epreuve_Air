import sys
#Vérification de la validité des arguments

if len(sys.argv) == 2:
    print("Error: Le programme nécessite deux arguments .")
    sys.exit(1)

#Récupération du tableau de chaine de caractères et de la chaine à la rechercher

array_de_string = sys.argv[1].split(',')
string = sys.argv[2]

#Fonction pour filtrer le tableau

def ma_fonction(array_de_string, string):
    nouvel_array_de_strings = []
    for element in array_de_string:
        if string in element:
            nouvel_array_de_strings.append(element)
    return nouvel_array_de_strings

#Affichage du nouveau tableau de chaine de caractères
print(ma_fonction(array_de_string, string))

# nouvel_array_de_strings