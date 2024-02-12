import sys 

def ma_fonction(string_a_couper, string_separateur):
    if len(sys.argv) != 3:
      print("Error: Le programme nécessite deux arguments.")
      sys.exit(1)
    tableau = string_a_couper.split(string_separateur)
    return tableau

if __name__=="__main__":
    if len(sys.argv) != 3:
        print("Error: Le programme nécessite deux arguments .")
        sys.exit(1)
    resultat = ma_fonction(sys.argv[1], sys.argv[2])
    print(resultat)

            

