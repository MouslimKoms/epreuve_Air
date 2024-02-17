import sys 

if len(sys.argv) != 2:
    print("Error : Le programme nécessite un seul argument, le nom du fichier ")
    sys.exit(1)

file_name = sys.argv[1]
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: Le fichier {file_name} est introuvable.")
    sys.exit(1)
except Exception as e:
    print(f"Error : Une erreur s'est produite lors de la lecture du fichier")
    sys.exit(1)