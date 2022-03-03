import sys
H,W = map(int,input().split())
A = [[0]*W for i in range(H)]
for h in range(H):
  A[h] = list(map(int,input().split()))
for h in range(H):
  for w in range(W):
    for j in range(h,H):
      for i in range(w,W):
        if A[h][w]+A[j][i] > A[j][w]+A[h][i]:
          print("No")
          sys.exit()
print("Yes")
