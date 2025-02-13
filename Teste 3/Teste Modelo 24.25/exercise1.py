def passing(students):
    aprovados = []
    
    for code, grade in students:
        if grade >= 9.5:
            aprovados.append(code)
            
    return aprovados

#print(passing([("up103", 7.4), ("up022", 14.5), ("up190", 10.5)]))
#print(passing([("up003", 7.4), ("up022", 4.5)]))
#print(passing([("up033", 13.4), ("up022", 6.5), ("up142", 16.5), ("up019", 17.5)]))
#print(passing([]))