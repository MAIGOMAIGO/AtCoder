N,K = map(int,input().split())
A = list(map(int,input().split()))
D = dict()
for i in A:
  if i in D:
    D[i] += 1
  else:
    D[i] = 1
if len(D) > K:
  x = len(D)-K
  L = [v for v in D.values()]
  L.sort()
  print(sum(L[:x]))
else:
  print(0)
