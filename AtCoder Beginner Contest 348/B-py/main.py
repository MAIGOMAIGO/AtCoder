N = int(input())
L = []
for i in range(N):
  X,Y = map(int, input().split())
  L.append((X,Y))
for i in range(N):
  m,p = 0,-1
  for j in range(N):
    if i != j:
      d = (L[i][0]-L[j][0])**2 + (L[i][1]-L[j][1])**2
      if m < d:
        m = d
        p = j
  print(p+1)