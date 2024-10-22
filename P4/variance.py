def sum_numbers(number):
    res = 0
    average = 0
    for i in range(1, number+1):
        res = res + i
        average = average + 1
    res = res/average
    return res

def var_numbers(number, precision):
    form = 