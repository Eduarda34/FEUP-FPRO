def isTriangulo(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def triangulars(n):
    resOdd = 0
    resEven = 0
    total = 0
    
    for i in range(1, n+1):
        if i%2 == 0:
            resEven += isTriangulo(i)
            
        else:
            resOdd += (isTriangulo(i) + isTriangulo(i+1))
            
    total = resOdd + resEven
    return total