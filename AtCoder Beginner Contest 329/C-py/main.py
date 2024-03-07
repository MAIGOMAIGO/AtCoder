N = int(input())
S = input()
D = dict()
c = 1
for i in range(N-1):
  if S[i] == S[i+1]:
    c += 1
  else:
    if S[i] in D:
      if D[S[i]] < c:
        D[S[i]] = c
    else:
      D[S[i]] = c
    c = 1
if S[-1] in D:
  if D[S[-1]] < c:
    D[S[-1]] = c
else:
  D[S[-1]] = c
a = 0
for i in D.keys():
  a += D[i]
print(a)
