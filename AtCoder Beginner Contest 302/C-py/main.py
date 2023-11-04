import itertools
N,M = map(int,input().split())
S = []
for i in range(N):
  S.append(input())
L = list(itertools.permutations(S))
for i in range(len(L)):
  f = 0
  for j in range(N-1):
    x = 0
    for k in range(M):
      if L[i][j][k] != L[i][j+1][k]:
        x += 1
    if x == 1:
      f += 1
  if f == N-1:
    print("Yes")
    exit(0)
print("No")
