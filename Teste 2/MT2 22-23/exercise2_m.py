def primo(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number%i == 0:
            return False
    return True

def next_prime(number):
    number += 1
    
    while not primo(number):
        number += 1
        
    return number

print(next_prime(10))
print(next_prime(13))
print(next_prime(26))
print(next_prime(450))