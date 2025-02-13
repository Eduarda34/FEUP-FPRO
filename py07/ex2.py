def vote(votes):
    counter = {}
    
    #percorre a lista de candidatos
    for candidato in votes:
        #e vai atualizar o dicionário
        if candidato in counter:
            counter[candidato] += 1
            
        else:
            counter[candidato] = 1
            
    #max com argumento key como "counter" para encontrar o candidato com maior número de votos
    winner = max(counter, key=counter.get)
    
    return winner

print(vote(['Flex', 'Flex', 'Flox', 'Flix', 'Flox', 'Flex', 'Flux']))
print(vote(['Flex', 'Flix', 'Flox', 'Flix', 'Flox', 'Flox', 'Flex']))