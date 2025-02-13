a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("Equilateral")
    
elif a == b or a == c or b == c:
    print("Isosceles")

else:
    if a + b > c and b + c > a and a + c > b:
        print("Scalene")
        
    else:
        print("Invalid")