N,T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))
m = 0
p = 0
if T in C:
  for i in range(N):
    if C[i] == T:
      if m < R[i]:
        m = R[i]
        p = i+1
else:
  c = C[0]
  for i in range(N):
    if c == C[i]:
      if m < R[i]:
        m = R[i]
        p = i+1
print(p)
