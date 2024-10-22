n1 = int(input())
n2 = int(input())
n3 = int(input())

n1 = (n1%5) + 2
n2 = (n2-5) * 3
n3 = n3//2

res1 = n1 * n2
res2 = res1 + n3

print(res1)
print(res2)