u = int(input())
v = int(input())

t = u
print(t)

while t != v:
    t = (t+u)%100
    if t == u:
        print("Pas trouvée")
        break
    elif t == v:
        print("v atteinte")
    else:
        print (t)
