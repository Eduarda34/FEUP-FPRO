def days_until_christmas(date):
    days_of_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }
    
    d, m, y = date
    restantes = 0
    
    while not (m == 12 and d == 25):
        restantes += 1
        d += 1
        
        if d > days_of_month[m]:
            d = 1
            m += 1
            
            if m > 12:
                m = 1
    
    return restantes


print(days_until_christmas((18,12,2022)))
print(days_until_christmas((25,12,2022)))
print(days_until_christmas((26,12,2022)))
print(days_until_christmas((10,1,2023)))