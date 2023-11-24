#>0 sum du reste <0 ajout de F ==0 égale 0
#définition sum

i = int(input())
ia = []
sum = 0
if i>0 :
  while i!=0:
    ii = int(input())
    ia.append(ii)
    i = i-1
  for v in ia:
    sum = sum + v
  print(sum)
elif i<0:
  while True:
    try:
      ii = int(input())
      ia.append(ii)
    except:
      break;
  for v in ia:
    sum = sum + v
  print(sum)
elif i==0:
  print(0)