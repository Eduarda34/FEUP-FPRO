def change(money):
    coins = [200,100,50,20,10,5,2,1]
    res = {}
    
    for moedita in coins: #iterar pelas moedas existentes
        #determina quantas moedas de x tipo são precisas    
        res[moedita] = money // moedita
            
        money = money % moedita #% -> resto
        
    return res

print(change(500))
print(change(523))
print(change(771))
print(change(445))