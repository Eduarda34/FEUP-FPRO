pe1 = int(input())
pe2 = int(input())
pe3 = int(input())
pe4 = int(input())

if pe3 < 40 and pe4 < 40:
    print("RFF")
    
else:
    note = max(pe3, pe4)
    
    if pe1 > pe2 and note > pe2:
        final = (pe1+note)/2
        print(int(final))
        
    elif pe2> pe1 and note > pe1:
        final = (pe2+note)/2
        print(int(final))
        
    else:
        final = (pe1+pe2)/2
        print(int(final))