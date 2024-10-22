num = int(input())
reverse = 0

while num > 0:
    ult = num%10  #modulo
    reverse = reverse*10 + ult
    
    num = num//10  #vai buscar a parte inteira
    
print(reverse)