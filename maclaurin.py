it = 1 #int temp
i = 1
ia = [] #int array
vt = 1 #valeur temp
vta = [] #valeur temp array
x = float(input())
t = 0 #temp


while it < 10**600: 
  for v in range(1, i + 1): 
    #1 à 1, 
    #1 à 3, 1*1 2*1 3*2 = 6
    #1 à 5, 6*1 2*6 3*12 4*36 5*144
    #1 à 7  144*1 2 3 4 5 6 7
    it = it * v
  ia.append(i)
  i = i + 2

for v in ia: #1,3,5,7,9...
  for w in range(1,v+1): #1 à 1, 1 à 3...
    vt = vt*w #1*1 1*2 2*3 1 2 3
    if w == v: #si w == 3 dans le v
      vta.append(vt) #ajout de 6
      vt = 1

for v in range(0,len(ia)):
  if v%2==0:
    t = t + x**ia[v]/vta[v]
  elif v%2!=0:
    t = t - x**ia[v]/vta[v]
print(t)

