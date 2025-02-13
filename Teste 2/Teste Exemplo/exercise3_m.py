example = {('Coimbra', 'Porto'): 125,
           ('Coimbra', 'Lisboa'): 200,
           ('Coimbra', 'Viseu'): 90,
           ('Porto', 'Braga'): 55,
           ('Braga', 'Vigo'): 110} 

def total_distance(dist, cities):
    distTotal = 0
    
    for i in range(len(cities) -1):
        city1 = cities[i]
        city2 = cities[i+1]
        
        if (city1, city2) in dist:
            distTotal += dist[(city1, city2)]
            
        elif (city2, city1) in dist:
            distTotal += dist[(city2, city1)]
            
        else:
            return -1 
        
    return distTotal

#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Lisboa']))
#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Viseu','Coimbra']))
#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Lisboa', 'Coimbra']))
#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Lisboa','Coimbra','Porto','Braga','Vigo']))
#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto']))