N,M = map(int,input().split())
S = []
for i in range(N):
  S.append(input())
c = 0
for i in range(N-1):
  for j in range(i+1,N):
    s = 0
    for k in range(M):
      s += 1 if S[i][k] == 'o' or S[j][k] == 'o' else 0
    if s == M:
      c += 1
print(c)
