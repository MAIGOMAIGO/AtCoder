W,H,N = map(int,input().split())
L = [[0]*W for i in range(H)]
for i in range(N):
  x,y,a = map(int,input().split())
  if a == 1:
    L = [[1]*x + j[x:] for j in L]
  elif a == 2:
    L = [j[:x] + [1]*(W-x) for j in L]
  elif a == 3:
    L = [[1]*W]*y + L[y:]
  elif a == 4:
    L = L[:y] + [[1]*W]*(H-y)
c = 0
for i in L:
  c += i.count(0)
print(c)
