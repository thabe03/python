import operator

def arithmetic_operator(sa):
  nsa = []
  ops = { "+": operator.add, "-": operator.sub }
  for i in range(len(sa)):
    nsa.append(sa[i].split())
  for l in range(len(nsa)):
    ans = ops[nsa[l][1]](int(nsa[l][0]),int(nsa[l][2]))
    print(nsa[l][0],nsa[l][1],nsa[l][2],"=",ans)

arithmetic_operator(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])