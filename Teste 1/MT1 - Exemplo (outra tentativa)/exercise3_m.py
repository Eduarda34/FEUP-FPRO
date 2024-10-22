import math

def approx_cos(x,n):
    res = 0
    
    for i in range(n):
        form = ((-1)**i / (math.factorial(2*i)) * (x**(2*i)))
        res = res + form
        
    return round(res, 5)