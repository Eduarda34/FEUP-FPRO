def sum_odd_even(number):    
     oddSum = 0
     evenSum = 0
     
     while number!=0:
         d = number%10
         if d%2 == 0:
             evenSum += d
         else:
             oddSum += d
             
         number = number//10
         
     if evenSum == oddSum:
         return f'identical sum = {evenSum}'
     
     else:
         return f'even sum = {evenSum}, odd sum = {oddSum}'
     
print(sum_odd_even(1234541))
print(sum_odd_even(234567))
print(sum_odd_even(123))
print(sum_odd_even(12345678))