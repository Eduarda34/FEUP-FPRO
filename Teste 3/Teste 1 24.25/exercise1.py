import math

a = int(input())
b = int(input())
c = int(input())

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(round(area,2))