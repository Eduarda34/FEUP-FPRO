h = int(input())
m = int(input())

if (h < 24 and m < 60):
    if h < 12:
        period = "am"
    else: 
        period = "pm"
        
    if h == 0:
        finalH = 12
        
    elif h <= 12:
        finalH = h
        
    else:
        finalH = h - 12
        
    if m == 0:
        print(str(finalH) + " " + period)
        
    else:
        if m < 10:
            finalM = "0" + str(m)
        
        else:
            finalM = str(m)
            
        print(str(finalH) + ":" + finalM + " " + period)
        
else:
    print("INVALID DATE FORMAT")