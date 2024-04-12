import random

def get_numbers_ticket(min, max, quantity):
   if min >= 1 and max <= 1000:
       lottery_numbers = random.sample(range(min, max+1), quantity)
       lottery_numbers.sort()
   else:         
       lottery_numbers = []        

   print(lottery_numbers)

get_numbers_ticket(1,49,6)