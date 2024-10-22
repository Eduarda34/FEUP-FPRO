h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

if h1 == h2:
    if m1 == m2: print("identical times")
    elif m1 > m2: print(f'{h1:02d}:{m1:02d} is after {h2:02d}:{m2:02d}')
    else: print(f'{h1:02d}:{m1:02d} is before {h2:02d}:{m2:02d}')
    
elif h1 > h2:
    print(f'{h1:02d}:{m1:02d} is after {h2:02d}:{m2:02d}')
    
else:
    print(f'{h1:02d}:{m1:02d} is before {h2:02d}:{m2:02d}')