def x_union(list1, list2): 
    proj_list1 = list(map(lambda x: x[0], list1))
    proj_list2 = list(map(lambda x: x[0], list2))
    
    unique_list1 = filter(lambda x: x[0] not in proj_list2, list1)
    unique_list2 = filter(lambda x: x[0] not in proj_list1, list2)
    
    return list(unique_list1) + list(unique_list2)