N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
m = 1
c = 0
for i in range(N-1):
  while A[i]+M > A[c]:
    c += 1
    if c >= N: break
  m = max(m,c-i)
  if c >= N: break
print(m)