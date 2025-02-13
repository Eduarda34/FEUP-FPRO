def bounded_mult(v,s,b):
    x, y = v
    width, height = b

    if x > width or y > height:
        return None
    
    else:
        limite = ((s*x) % width, (s*y) % height)
        return limite
    
print(bounded_mult((10, 20), 2, (50, 50)))
print(bounded_mult((10, 20), 3, (50, 50)))
print(bounded_mult((20, 10), 5, (30, 50)))
print(bounded_mult((60, 20), 2, (50, 50)))