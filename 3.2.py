import random

def get_numbers_ticket(min, max, quantity):
    
   if 1 <= min <= max < 1000 and quantity < max - min:
      lottery_numbers = random.sample(range(min, max+1), quantity)
      lottery_numbers.sort()
   else:         
      lottery_numbers = []        
   
   return lottery_numbers

result = get_numbers_ticket(10,6,6)
print(result)