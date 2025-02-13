def switch_dict(adict):    #adict = dicionario
    newDict = {}
    
    for key, value in adict.items():
        if value in newDict:
            newDict[value].append(key)
            
        else:
            newDict[value] = [key]
            
    return newDict

#print(switch_dict({"jan": "winter", "feb": "winter", "may": "spring", "july": "summer", "august": "summer"}))
#print(switch_dict({1: 2, 2: 1, 3: 1, 4: 2}))
#print(switch_dict({"Ice": "Cream", "Heavy": "Cream", "Light": "Cream", "Double": "Cream"}))
#print(switch_dict({}))