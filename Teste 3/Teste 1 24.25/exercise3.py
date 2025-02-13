x = int(input())

# // --> divisão inteira (arredondado para baixo)

if (x%2 == 0):
    for i in range(x):
        print("#"*((x-1) // 2) + "00" + "#"*((x-1) // 2))
        #primeiro adiciona uma sequência de # de comprimento (x-1)//2
        #em seguida, adiciona dois zeros no centro
        #por fim, adiciona outra sequência de # de comprimentos (x-1)//2

else:
    for i in range(x):
        print("#"*(x//2) + "0" + "#"*(x//2))