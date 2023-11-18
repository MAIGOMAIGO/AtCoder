import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)

N,D = map(int,input().split())
L = []
for i in range(N):
  X,Y = map(int,input().split())
  L.append([X,Y,False])

@lru_cache(maxsize=2000)
def f(v):
  if not L[v][2]:
    L[v][2] = True
    for i in range(N):
      if not L[i][2]:
        u = ((L[v][0]-L[i][0])**2) + ((L[v][1]-L[i][1])**2)
        if u <= D**2:
          f(i)

if N > 1:
  f(0)
else:
  L[0][2] = True
for i in range(N):
  print("Yes" if L[i][2] else "No")
