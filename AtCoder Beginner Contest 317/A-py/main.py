N,H,X = map(int,input().split())
P = list(map(int,input().split()))
L = []
for i in range(N):
  if H+P[i] >= X:
    L.append((H+P[i],i))
print(min(L)[1]+1)
