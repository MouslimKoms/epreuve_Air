import sys

def ma_fonction(string_a_couper , string_separateur):
    
    if len(sys.argv) != 2:
        print ("Error: Le programme nécessiste une chaine de caractère à découper en argument.")
        sys.exit(1)
    
    tableau = string_a_couper.split()
    return tableau

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error : Le programme nécessiste une chaine de caractère à découper en argument.")
        sys.exit(1)
    resultat = ma_fonction(sys.argv[1], " ")
    print(resultat)
    
    
