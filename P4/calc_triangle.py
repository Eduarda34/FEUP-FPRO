def calc_triangular(n):
    res = 0
    if n == 1:
        return 1
    
    for i in range(1, n+1):
        res = res + i
        
    return res

#print(calc_triangular(1))
#print(calc_triangular(3))
#print(calc_triangular(10))
#print(calc_triangular(23))