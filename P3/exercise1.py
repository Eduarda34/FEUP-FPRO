num = int(input())

for index in range(1, 11):
    if num == index:
        res = num**2
        print(f"{num} ^ 2 = {res}")
        break
        
    else:
        res = num * index
        print(f"{num} x {index} = {res}")