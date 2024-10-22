import math

g = 9.81

l = float(input())

t = 2*math.pi * math.sqrt(l/g)

print(round(t,2))