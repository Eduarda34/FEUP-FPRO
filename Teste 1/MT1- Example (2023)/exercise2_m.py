p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())

if p3 < 40 and p4 < 40:
    print("RFF")
    
else:
    note = max(p3, p4)
    
    if p1 > p2 and note > p2:
        final = (p1+note)/2
        print(int(final))
        
    elif p2 > p1 and note > p1:
        final = (p2+note)/2
        print(int(final))
        
    else:
        final = (p1+p2)/2
        print(int(final))