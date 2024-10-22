import math

def approx_pi(n):
    res = 0
    
    for i in range(n):
        form = ((-1)**i) / (2*i + 1)
        res = res + form
        
    res = res*4
    
    return round(res, 5)

print(approx_pi(10))
print(approx_pi(100))
print(approx_pi(1000))
print(approx_pi(10000))