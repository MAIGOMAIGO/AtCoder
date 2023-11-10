N,M = map(int,input().split())
S = set()
for i in range(1,N+1):
  for j in range(i+1,N+1):
    S.add((i,j))
for i in range(M):
  a = input().split()
  for j in range(N-1):
    s1,s2 = int(a[j]),int(a[j+1])
    S.discard((min(s1,s2),max(s1,s2)))
print(len(S))
