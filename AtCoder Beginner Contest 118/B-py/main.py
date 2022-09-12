N,M = map(int,input().split())
A = []
for i in range(N):
  KA = list(map(int,input().split()))
  A.append(KA[1:])
c = 0
for i in range(1,M+1):
  f = True
  for j in range(N):
    if not i in A[j]:
      f = False
      break
  if f:
    c += 1
print(c)
