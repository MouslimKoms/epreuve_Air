
import os
import subprocess
import sys


folder_path = sys.argv[1]

for filename in os.listdir(folder_path) :
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        try:
            subprocess.run(["python",file_path], check=True)
            print(f"Le fichier {filename} fonctionne correctement.")
        except subprocess.CalleProcessError:
            print(f"Erreur : Le fichier {filename} n'a pas fonctionné correctement. ")
