N,M = map(int, input().split())
L = [[0] * N for i in range(N)]
for i in range(M):
  U,V = map(int, input().split())
  L[U-1][V-1] = 1
  L[V-1][U-1] = 1
c = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if L[i][j] and L[j][k] and L[k][i]:
        c += 1
print(c)
