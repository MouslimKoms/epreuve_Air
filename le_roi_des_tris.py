import sys

if len(sys.argv) < 2:
    print("Error : Le programme nécessite au moins une liste de nombres à trier")
    sys.exit(1)

array = list(map(int, sys.argv[1:]))

def my_quick_sort(array):
    if len(array) <= 1 : 
        return array 
    else:
        pivot = array[0]
        less_than_pivot = [ x for x in array [1:] if x <= pivot]
        greater_than_pivot = [ x for x in array [1:] if x > pivot]
        return my_quick_sort(less_than_pivot) + [pivot] + my_quick_sort(greater_than_pivot)
print(my_quick_sort(array))