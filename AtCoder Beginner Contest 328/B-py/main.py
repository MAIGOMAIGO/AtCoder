N = int(input())
D = list(map(int,input().split()))
c = 0
for i in range(N):
  for j in range(D[i]):
    s = str(i+1) + str(j+1)
    f = True
    for k in s:
      if s[0] != k:
        f = False
    if f:
      c += 1
print(c)
