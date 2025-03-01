from functools import reduce as r

def bounding_box(pts):
    x = list(map(lambda x: x[0], pts))
    y = list(map(lambda y: y[1], pts))
    
    return (r(lambda i,j: i if i<j else j, x),
            r(lambda i,j: i if i<j else j, y),
            r(lambda i,j: i if i>j else j, x),
            r(lambda i,j: i if i>j else j, y))