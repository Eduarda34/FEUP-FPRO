n = int(input())
div = n//2

if(n%2 != 0): #se for impar
    for i in range(0, n):
        for j in range(0, n):
            if (j == div) and (i == div):
                print("0", end = "")
                
            else:
                print("#", end = "")
                
        print(end = '\n')
        
else:
    for i in range(0, n):
        for j in range(0, n):
            if ((j == div) or (j == div-1)) and ((i == div) or (i == div-1)):
                print("0", end = "")
                
            else:
                print("#", end = "")
                
        print(end = '\n')