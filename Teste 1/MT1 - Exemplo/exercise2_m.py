p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())

if p3 < 40 and p4 < 40:
    print("RFF")  

else: 
    note = max(p3, p4)
    if note > p1 and p1 > p2:
        final = (note + p1) / 2
        print(int(final))

    elif note > p2 and p2 > p1:
        final = (note + p2) / 2
        print(int(final))
    
    elif p1 > note and note > p2:
        final = (note + p1) / 2
        print(int(final))
    
    elif p2 > note and note > p1:
        final = (note + p2) / 2
        print(int(final))
    
    else:
        final = (p2 + p1) / 2
        print(int(final))