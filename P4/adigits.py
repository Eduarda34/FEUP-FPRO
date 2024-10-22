def adigits(a,b,c):
    res = 0
    
    if a <= b and a <= c:
        res = a*100
        if b <= c:
            res = res + b*10 + c
        
        else: res = res + c*10 + b
        
    elif b <= a and b <= c:
        res = b*100
        if a <= c:
            res = res + a*10 + c
            
        else: res = res + c*10 + a
        
    elif c <= a and c <= b:
        res = c*100
        if a <= b:
            res =  res + a*10 + b
        
        else: res = res + b*10 + a
        
    return res

#print(adigits(1, 2, 3))
#print(adigits(9, 1, 9))
#print(adigits(9, 1, 8))
#print(adigits(0, 1, 0))