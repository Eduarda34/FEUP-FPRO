def calc_triangular(n): #reutilizada do ex.2
    res = 0
    if n == 1:
        return 1
    
    for i in range(1, n+1):
        res = res + i
        
    return res

def calc_factorial(n):
    res = 0
    if n == 1:
        return 1
    for i in range(1, n+1):
        res = res * i
    return res

def reuse(number):
    res = 0
    for i in range(1, number+1):
        if i%2 == 0:
            res = res + calc_triangular(i)
        else:
            res = res + calc_factorial(i)
    return res

print(reuse(1))
print(reuse(3))
print(reuse(6))
print(reuse(10))