N,D = map(int,input().split())
X = []
for i in range(N):
  X.append(list(map(int,input().split())))
c = 0
for i in range(N-1):
  for j in range(i+1,N):
    L = []
    for k in range(D):
      L.append((X[i][k]-X[j][k])**2)
    if (sum(L)**0.5).is_integer():
      c += 1
print(c)
