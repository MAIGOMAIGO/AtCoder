N = int(input())
A = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
  kx = list(map(int,input().split()))
  if kx[0] == 1:
    A[kx[1]-1] = kx[2]
  elif kx[0] == 2:
    print(A[kx[1]-1])
