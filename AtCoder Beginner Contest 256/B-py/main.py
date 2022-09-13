N = int(input())
A = list(map(int,input().split()))
P = 0
m = [-1,-1,-1,-1]
for i in range(N):
  m[0] = i
  for j in range(3,-1,-1):
    if m[j] >= 0:
      if j+A[i] >= 4:
        P += 1
      else:
        m[j+A[i]] = m[j]
      m[j] = -1
print(P)
