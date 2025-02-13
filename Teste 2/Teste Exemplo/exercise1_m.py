def time_diff(time1, time2):
    h1, m1 = time1
    h2, m2 = time2
    
    minutos1 = h1*60 + m1
    minutos2 = h2*60 + m2
    
    minTotal = abs(minutos1 - minutos2)
    
    horasFinais = minTotal // 60
    minutosFinais = minTotal % 60
    
    return (horasFinais, minutosFinais)

#print(time_diff((14, 30), (17, 45)))
#print(time_diff((10, 25), (10, 20)))
#print(time_diff((19,30), (17, 00)))
#print(time_diff((10, 45), (10, 45)))