H,W = map(int,input().split())
A = []
for i in range(H):
  L = list(map(int,input().split()))
  A.append(L)
for i in range(W):
  B = []
  for j in range(H):
    B.append(A[j][i])
  print(' '.join(map(str,B)))
