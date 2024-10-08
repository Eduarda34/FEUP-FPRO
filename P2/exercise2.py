n = int(input())
n1 = n%1000
n2 = n1%100
n3 = n2%10

#divisao inteira -> //
r1 = n // 1000 * 1000
r2 = n1 // 100 * 100
r3 = n2 // 10 * 10
r4 = n3 // 1

print(r1)
print(r2)
print(r3)
print(r4)