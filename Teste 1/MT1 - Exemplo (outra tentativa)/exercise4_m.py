def check_friendly(number_one, number_two):
    if number_one == number_two:
        return f'identical numbers: {number_one}'
    
    else:
        res1 = 0
        res2 = 0
        
        for i in range(1, number_one):
            if number_one%i == 0:
                res1 = res1 + i
                
        for i in range(1, number_two):
            if number_two%i == 0:
                res2 = res2 + i
                
        if res1 != number_two:
            return f'sum of divisors of {number_one} is not {number_two}'
        
        elif res2 != number_one:
            return f'sum of divisors of {number_two} is not {number_one}'
        
        else:
            return f'{number_one} and {number_two} are friendly'
        