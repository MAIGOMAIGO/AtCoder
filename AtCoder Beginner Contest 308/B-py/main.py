N,M = map(int,input().split())
C = list(map(str,input().split()))
D = list(map(str,input().split()))
P = list(map(int,input().split()))
c = 0
for i in range(N):
  if C[i] in D:
    c += P[D.index(C[i])+1]
  else:
    c += P[0]
print(c)
