def sparse_dot_product(dict1, dict2):
    res = 0
    
    for key, value in dict1.items():
        if key in dict2:
            res += value * dict2[key]
            
    return res

#print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))
#print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))
#print(sparse_dot_product({10: 10, 3: 5}, {1: 10, 3: 1}))
#print(sparse_dot_product({2: 90, 9: 80, 1: -5, 8: 7}, {2: -4, 9: 1, 1: 6}))