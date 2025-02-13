def mask_data(data, n_characters, position):
    res = ""
    
    if (n_characters == 0): return data
    
    if (position == "begin"):
        for i in range(0, n_characters+1):
            res = n_characters * "*" + data[n_characters:]
            
    else:
        for i in range(0, len(data) - n_characters):
            res = data[0:len(data) - n_characters] + n_characters * "*"
                
    return res