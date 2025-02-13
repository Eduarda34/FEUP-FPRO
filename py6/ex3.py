def rotate_list(l): #l é uma lista
    for index in range(3): #executar as 3 rotações
        element = l.pop(0) #remove o primeiro elemento
        l.append(element)
        
    return l