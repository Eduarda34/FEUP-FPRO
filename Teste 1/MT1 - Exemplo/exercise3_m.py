import math

def approx_cos(x,n):
    res = 0
    
    for i in range(n):
        form = ((-1)**i / (math.factorial(2*i)) * x**(2*i))
        res = res + form
    
    return round(res, 5)


print(approx_cos(1.0, 3))
print(approx_cos(2.0, 3))
print(approx_cos(1.0, 5))
print(approx_cos(-1.0, 10))