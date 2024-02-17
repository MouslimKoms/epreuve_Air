import sys 

if len(sys.argv) < 2 :
    print("Error: Le programme nécessite au moins un argument .")
    sys.ext(1)

array = sys.argv[1:]

def ma_rotation(array):
    first_element = array[0]
    for i in range(len(array)-1):
        array[i] = array[i + 1]
    array[-1] = first_element
    return array 
print(ma_rotation(array))