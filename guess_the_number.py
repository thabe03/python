#possiblité
#définition
import random
s = random.randint(0, 100)
print(s)
x = 0;
while x!=6:
  i = int(input())
  x = x+1
  if i == s:
    print("Gagné en",x,"essai(s) !")
    break;
  elif x == 6:
    print("Perdu ! Le secret était",s)
    break;
  elif i > s:
    print("Trop grand")
  elif i < s:
    print("Trop petit")

