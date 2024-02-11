import sys 

def ma_fonction(string_a_couper, string_separateur):
    if not isinstance(string_a_couper, str) or not isinstance(string_separateur, str):
        print("Error: Les arguments doivent etre des chaines de caractères.")
        sys.exit(1)
        
    tableau = [ ] 
    element = " "
    for char in string_a_couper:
        if char != string_separateur:
            element += char
        else:
            tableau.append(element)
            element = " "
    tableau.append(element)
    return tableau 
    
            

