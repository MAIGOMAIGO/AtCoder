N,M = map(int,input().split())
ab = []
for i in range(N):
  ab.append(list(map(int,input().split())))
cd = []
for i in range(M):
  cd.append(list(map(int,input().split())))
for i in range(N):
  m = abs(ab[i][0]-cd[0][0]) + abs(ab[i][1]-cd[0][1])
  c = 0
  for j in range(1,M):
    if m > abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1]):
      m = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1])
      c = j
  print(c+1)
