n1 = int(input())
n2 = int(input())
result = 0

while n1 != 0:
    d1 = n1%10 #modulo
    d2 = n2%10
    
    result = result*100 + d1*10 + d2
    
    n1 = n1//10 #parte inteira
    n2 = n2//10
    
print(result)