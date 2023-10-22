H,W = map(int,input().split())
A = []
B = []
for i in range(H):
  A.append(input())
for i in range(H):
  B.append(input())
for i in range(H):
  b = B[i:] + B[:i]
  for j in range(W):
    f = True
    for k in range(H):
      if A[k] != b[k][j:] + b[k][:j]:
        f = False
    if f:
      print("Yes")
      exit(0)
print("No")
