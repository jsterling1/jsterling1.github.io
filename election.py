from random import randint
wins = 0

for i in range(10000): #repeat the process a thousand times
  regions=0
  if randint(1,100) <= 87:
    regions = regions + 1 #add to the amount of wins
   if randint(1,100) <= 65:
    regions = regions + 1 #add to the amount of wins
   if randint(1,100) <= 17:
    regions = regions + 1 #add to the amount of wins
  if regions >= 2:
    wins = wins + 1


