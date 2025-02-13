def time_add(time, delta):
    h, m = time
    
    minutos = h*60 + m
    
    minutos += delta
    
    horasFinais = minutos // 60 
    minutosFinais = minutos % 60
    
    if horasFinais == 24:
        horasFinais = 0
    
    return (horasFinais, minutosFinais)

print(time_add((15,10), 70))
print(time_add((17,45), 150))
print(time_add((23,30), 45))
print(time_add((10,45), 0))