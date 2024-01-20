N = int(input())
F,S = [],[]
for i in range(N):
  f,s = map(int,input().split())
  F.append(f)
  S.append(s)
si = S.index(max(S))
M = (si,max(S))
m = 0
for i in range(N):
  if i != si:
    if F[si] == F[i]:
      m = max(m,M[1]+S[i]//2)
    else:
      m = max(m,M[1]+S[i])
print(m)
