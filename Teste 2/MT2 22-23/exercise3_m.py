example = {('Porto', 'Coimbra'): 125,
           ('Coimbra', 'Lisboa'): 200,
           ('Porto', 'Aveiro'): 50,
           ('Aveiro', 'Lisboa'): 250}

def shortest_path(dist, start, end):
    minDist = 0
    
    if (start, end) in dist:
        minDist = dist[(start, end)]
        
    for (city1, city2), distance in dist.items():
        if city1 == start:
            if (city2 == end) in dist:
                totalDist = distance + dist[(city2, end)]