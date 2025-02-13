def camel_case(phrase):
    res = ""
    upper = False
    
    for ch in phrase:
        if (ch.isalpha()):
            if upper:
                res += ch.upper()
                upper = False
                
            else:
                res += ch.lower()
            
        else:
            upper = True
            
    return res