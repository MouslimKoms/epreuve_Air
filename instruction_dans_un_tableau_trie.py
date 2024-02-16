
import sys
if len(sys.argv) < 3:
    print("Error : Le programme nécessite deux arguments .")
    sys.exit(1)


array = [int (x) for x in sys.argv[1:-1]]
new_element = int(sys.argv[-1])

def sort_insert(array,new_element):
    index = 0
    for i in range(len(array)):
        if array[i] > new_element:
           
            
            break
        else:
            index = i + 1 
    array.insert(index,new_element)
    return array
print(sort_insert(array,new_element))


