N,K = map(int,input().split())
D = dict()
for i in range(N):
  a,b = map(int,input().split())
  if a in D:
    D[a] += b
  else:
    D[a] = b
L = sorted(D.keys())
s = sum(D.values())
if N > 1:
  D[L[0]] = s-D[L[0]]
if D[L[0]] <= K:
  print(1)
  exit(0)
for i in range(1,len(L)):
  D[L[i]] = D[L[i-1]] - D[L[i]]
  if D[L[i]] <= K:
    print(L[i]+1)
    exit(0)
print(L[i]+1)
