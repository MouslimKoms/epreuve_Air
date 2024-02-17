import sys 

if len(sys.argv) != 3:
    print("Error: Le programme nécessite deux arguments, le caractère et le nombre d'étage ")
    sys.exit(1)
    
character = sys.argv[1]
num_floors = int(sys.argv[2])

for i in range(1,num_floors+1):
    print(character * i)