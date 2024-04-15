N = int(input())
S = input()
D = {chr(i+97):[] for i in range(26)}
for i in range(N):
  D[S[i]].append(i)
Q = int(input())
for i in range(Q):
  c,d = map(str, input().split())
  if c != d:
    if c in D:
      if d in D:
        D[d] += D[c]
        del D[c]
      else:
        D[d] = D[c]
        del D[c]
L = [""] * N
for i in D.keys():
  for j in D[i]:
    L[j] = i
print("".join(L))
