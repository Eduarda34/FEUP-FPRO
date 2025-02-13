def variance(alist):
    n = len(alist)
    mean = sum(alist) / n
    squared_diff = map(lambda x: (x - mean)**2, alist)
    result = sum(squared_diff) / n
    
    return round(result, 3)