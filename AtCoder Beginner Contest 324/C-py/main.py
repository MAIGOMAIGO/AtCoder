N,T = map(str,input().split())
N = int(N)
K = 0
i = list()
for j in range(1,N+1):
  S = input()
  if len(T) == len(S):
    c = 0
    for k in range(len(T)):
      if T[k] != S[k]:
        c += 1
    if c < 2:
      K += 1
      i.append(j)
  elif len(T)+1 == len(S):
    c = 0
    f = True
    for k in range(len(T)):
      if c == 0 and T[k] != S[k]:
        if T[k] != S[k+1]:
          f = False
          break
        c += 1
      elif c == 1 and T[k] != S[k+1]:
        f = False
        break
    if f:
      K += 1
      i.append(j)
  elif len(T)-1 == len(S):
    c = 0
    f = True
    for k in range(len(S)):
      if c == 0 and T[k] != S[k]:
        if T[k+1] != S[k]:
          f = False
          break
        c += 1
      elif c == 1 and T[k+1] != S[k]:
        f = False
        break
    if f:
      K += 1
      i.append(j)
print(K)
print(*i)
