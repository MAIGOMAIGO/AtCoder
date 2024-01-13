N,M = map(int,input().split())
S = input()
C = list(map(int,input().split()))
D = dict()
for i in range(N):
  if C[i] in D:
    D[C[i]] += S[i]
  else:
    D[C[i]] = S[i]
for i in range(M):
  if len(D[i+1]) > 1:
    D[i+1] = D[i+1][-1] + D[i+1][0:]
L = [0 for i in range(M)]
s = ""
for i in range(N):
  s += D[C[i]][L[C[i]-1]]
  L[C[i]-1] += 1
print(s)
