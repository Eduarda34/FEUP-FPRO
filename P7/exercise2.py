romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

def roman_to_integer(astring):
    total = 0
    comprim = len(astring)
    
    for i, c in enumerate(astring):
        if i < comprim-1 and romans[c] < romans[astring[i+1]]:
            total -= romans[c]
        
        else:
            total += romans[c]
            
    return total


#print(roman_to_integer('XV'))
#print(roman_to_integer('LXXXIV'))
#print(roman_to_integer('XLIII'))
#print(roman_to_integer('MMMCMXCIX'))