N,M = map(int,input().split())
kx = []
for i in range(M):
  kx.append(list(map(int,input().split())))
for i in range(N-1):
  for j in range(i+1,N):
    f = True
    for x in kx:
      if (i+1 in x[1:]) and (j+1 in x[1:]):
        f = False
        break
    if f:
      print("No")
      exit(0)
print("Yes")
