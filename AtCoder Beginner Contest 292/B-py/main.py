N,Q = map(int,input().split())
L = [0 for i in range(N)]
for i in range(Q):
  c,x = map(int,input().split())
  if c == 1:
    L[x-1] += 1
  elif c == 2:
    L[x-1] += 2
  elif c == 3:
    print("Yes" if L[x-1] >= 2 else "No")
