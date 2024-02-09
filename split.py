import sys


def ma_fonction(string_a_couper , string_separateur):
    if not string_a_couper or not string_separateur:
        print("Erreur : Les arguments ne doivent pas etre vides")
        sys.exit(1)
    tableau = []
    mot = ""
    for char in string_a_couper:
        if char in string_separateur:
            if mot:
                tableau.append(mot)
                mot = ""
        else:
            mot += char
    if mot:
        tableau.append(mot)
    return tableau

if len(sys.argv) != 3:
    print("Erreur : Veuillez fournir une chaine a découper et un séparateur")
    sys.exit(1)
    
    
resultat = ma_fonction(sys.argv[1], sys.argv[2])
print("Résultat du découpage :",resultat)