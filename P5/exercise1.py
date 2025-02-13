#podemos inverter primeiro e depois tirar as letras
#ou podemos tirar primeiro e depois inverter o res

def rm_letter_rev(ch, s):
    res = ""
    final = ""
    
    for i in s:
        if (i != ch):
            res += i
            
    final = res[::-1] #inverter a string
            
    return final