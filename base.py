import re  #regex
import os
import imageio
import urllib.request
import json
import random
import math

i = 5
p = 2
g = 10
s = "string char int"
f = "char"
c = "c"
t = "     trim,strip     "
cstdio = "I want {} pieces." #att dans react
n = None
ia = [21, 41, 12, 9, 74, 15]
sa = ["s", "t", "r", "i", "n", "g","i","n","t"]
o = {"o": "o o", "oo": "oo oo", "ooo": "ooo ooo"}
a = 'o'
ma = dict()
ma['ma'] = "ma"
class O:
    x = 0
    def __init__(self, x): #~constructor
        self.x = x
    def p(self):
      self.x = self.x + 1
    def f(self):
        print(self.x)
oo = O(i) #oo.p() oo.f()
ao = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
rJson = json.loads(ao)

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
print(s.find(c))  #premier index
print(len(s))

print(random.randrange(p, g))
print(random.randint(p,g))

for v in ia:
    if n is None or v < n:
        n = v  #tampon n devient la valeur
print(n)  #i
#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
print(o.get(a))
print(s[p:g])
print(t.strip())
print(s.upper())
print(cstdio.format(i))
print(s.replace(c,c))

print(rJson[1]['name'])

for k in o:
    if o[k] != "oo oo":
        print(k, o[k])  #s,s
for (k, v) in ma.items():
    print(k, v)  #k,v
print(i**i)
#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
print(f in s)
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
for v in s:
    print(v)  #c
  
#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIAAAAAAAAAAAAAAAAAAAAAA
print(sorted(ia, reverse=True))
print([x for x in range(i) if x*i==i])

for i in range(i):
  ia.append(i)
print(ia)
#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAAAAAAAAAAAAAAAAAAAAAA
print(s.split())  #whitespace default
print(re.findall('\s', s))
print([x for x in sa if "i" in x])

var=str(input("var="))
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#sa.append(i) #ajout fin
#sa.insert(i,s) #ajout contrôlé
#sa.extend(sa) #ressemble à .concat
#sa.remove(s) #sa.pop(i) #même chose
#sa.clear()
#sa.sort()
#sa.sort(reverse = True)

for i in urllib.request.urlopen('http://data.pr4e.org/romeo.txt'):
  print(i.decode()) #peut ajouter .strip()

