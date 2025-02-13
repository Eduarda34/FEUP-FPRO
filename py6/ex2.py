def nth_lowest(lnum, n): #lnum é uma lista
    small = []
    
    while len(small) < n:
        currMin = min(lnum)
        small.append(currMin)
        
        lnum.remove(currMin)
        
    return small[-1] 
    #o n-ésimo menor valor é o último a ser adicionado à lista
    

def nth_lowest2(lnum, n):
    sorted_list = sorted(lnum)
    
    # Retornar o n-ésimo menor valor (índice n-1)
    return sorted_list[n - 1]