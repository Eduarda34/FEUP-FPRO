def shopping(alist, stock):
    spent = 0
    missing = {}

    for item, quantity in alist.items():
        existing, price = stock.get(item, (0,0))
        delta = quantity - existing

        if delta > 0:
            missing[item] = delta

        spent += min(quantity, existing) * price

    return spent, missing

def normalize(result):
    (quant, adict) = result
    return (quant, sorted(adict.items()))

#print(normalize(shopping({'banana': 10, 'apples': 20, 'oranges': 30}, {'banana': (30, 3), 'apples': (10, 2)})))
#print(normalize(shopping({'banana': 10, 'apples': 20, 'oranges': 30}, {'banana': (10, 3), 'apples': (20, 2), 'oranges': (30, 1)})))
#print(normalize(shopping({'banana': 10, 'apples': 10, 'oranges': 10, 'kiwis': 5}, {'banana': (10, 3), 'apples': (20, 2), 'oranges': (30, 1)})))
#print(normalize(shopping({'banana': 10, 'apples': 10, 'oranges': 10, 'kiwis': 5}, {'banana': (5, 3), 'apples': (5, 2), 'oranges': (5, 1)})))