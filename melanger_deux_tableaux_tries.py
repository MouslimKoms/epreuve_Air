import sys

if len(sys.argv) < 3 or "fusion" not in sys.argv:
    print("Error : Le programme nécessite au moins deux liste d'entiers triées séparées par 'fusion'. ")
    sys. exit(1)

index_fusion = sys.argv.index("fusion")
array1 = list(map(int, sys.argv[1:index_fusion]))
array2 = list(map(int, sys.argv[index_fusion+1:]))

def sorted_fusion(array1, array2 ):
    new_array = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1
    new_array.extend(array1[i:])
    new_array.extend(array2[j:])
    return new_array


print(sorted_fusion(array1, array2))