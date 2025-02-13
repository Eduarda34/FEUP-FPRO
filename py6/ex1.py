def fib(n):
    fibo = [0,1] #são os primeiros números
    
    if n == 1:
        return [0]
    
    for i in range(2,n):
        number = fibo[-1] + fibo[-2] #soma os dois últimos números
        fibo.append(number)
        
    return fibo
    
    
print(fib(1))
print(fib(5))
print(fib(7))
print(fib(13))