N,Q = map(int,input().split())
S = input()
c = 0
L = [0] * N
P = [False] * N
for i in range(N-1):
  if S[i]==S[i+1]:
    c += 1
    P[i] = True
  L[i] = c
L[N-1] = c
for i in range(Q):
  l,r = map(int,input().split())
  if l<=r-1:
    print(L[r-2]-(L[l-1]-1 if P[l-1] else L[l-1]))
  else:
    print(0)
